#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <HardwareSerial.h>

// LCD Configuration
LiquidCrystal_I2C lcd(0x27, 16, 2); // Adjust address if needed

// Touch Input Pins
#define DIVE_PIN 4
#define RISE_PIN 15
#define FORWARD_PIN 14
#define LEFT_PIN 13
#define RIGHT_PIN 27
#define LIGHT_PIN 12

// Buzzer Pin
#define BUZZER_PIN 5

// RS485 Configuration
#define RS485_DIR_PIN 26
HardwareSerial RS485Serial(2); // UART2
int touchThreshold=90;
void setup() {
    // Initialize LCD
    lcd.init();
    lcd.backlight();
    lcd.setCursor(0, 0);
    lcd.print("Remote Control");

    // Initialize Pins
    pinMode(DIVE_PIN, INPUT);
    pinMode(RISE_PIN, INPUT);
    pinMode(FORWARD_PIN, INPUT);
    pinMode(LEFT_PIN, INPUT);
    pinMode(RIGHT_PIN, INPUT);
    pinMode(LIGHT_PIN, INPUT);

    pinMode(BUZZER_PIN, OUTPUT);
    pinMode(RS485_DIR_PIN, OUTPUT);

    // Initialize RS485
    RS485Serial.begin(9600, SERIAL_8N1, -1, -1); // RX, TX not defined since MAX485 handles it

    // Initial RS485 Direction Pin State (default to receiving mode)
    digitalWrite(RS485_DIR_PIN, LOW);
}

void loop() {
    uint8_t controlByte = 0;
    
    if (touchRead(DIVE_PIN) < touchThreshold) controlByte |= 0b00000001;
    if (touchRead(RISE_PIN) < touchThreshold) controlByte |= 0b00000010;
    if (touchRead(FORWARD_PIN) < touchThreshold) controlByte |= 0b00000100;
    if (touchRead(LEFT_PIN) < touchThreshold) controlByte |= 0b00001000;
    if (touchRead(RIGHT_PIN) < touchThreshold) controlByte |= 0b00010000;
    if (touchRead(LIGHT_PIN) < touchThreshold) controlByte |= 0b00100000;

    // Display status on LCD
    lcd.setCursor(0, 1);
    lcd.print("Status: ");
    //lcd.print(touchRead(LEFT_PIN));
    lcd.print(controlByte, BIN);
    lcd.print("    "); // Clear remaining spaces

    // Buzzer Activation
    if (controlByte != 0) {
        digitalWrite(BUZZER_PIN, HIGH);
    } else {
        digitalWrite(BUZZER_PIN, LOW);
    }

    // Send Data via RS485
    if (controlByte != 0) {
        digitalWrite(RS485_DIR_PIN, HIGH); // Set to Transmit mode
        delay(10); // Short delay to allow RS485 driver to switch modes
        RS485Serial.write(controlByte);
        RS485Serial.flush();
        digitalWrite(RS485_DIR_PIN, LOW); // Set back to Receive mode
    }

    delay(200); // Debounce delay for touch inputs
}
