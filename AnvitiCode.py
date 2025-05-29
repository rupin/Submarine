from machine import Pin, UART, TouchPad
import time

# Initialize UART2 and Direction Control pin
SerialPort = UART(2, baudrate=9600, tx=17, rx=16)  # Adjust TX/RX pins as needed

control_pin = Pin(26, Pin.OUT) 
#Set the control pin direction to Transmit
control_pin.value(1)

touch_pin_sink = TouchPad(Pin(4))
touch_pin_rise = TouchPad(Pin(12))
touch_pin_left = TouchPad(Pin(13))
touch_pin_right = TouchPad(Pin(14))
touch_pin_forward = TouchPad(Pin(15))
touch_pin_LED = TouchPad(Pin(27))

codeToSink=192
codeToRise=3
codeToGoLeft=32
codeToGoRight=4
codeToGoForward=8
codeToTurnOnLight=16

SerialPort.write(bytes([255]))
touchThreshold=200

while(True):
    time.sleep(0.1)
    touchValueSink=touch_pin_sink.read()
    if(touchValueSink<touchThreshold):
        #send the code to the submarine
        SerialPort.write(bytes([codeToSink]))
        

    touchValueRise=touch_pin_rise.read()
    if(touchValueRise<touchThreshold):
        #send the code to the submarine
        SerialPort.write(bytes([codeToRise]))
        
    touchValueLeft=touch_pin_left.read()
    if(touchValueRise<touchThreshold):
        #send the code to the submarine
        SerialPort.write(bytes([codeToGoLeft]))
        
    touchValueRight=touch_pin_right.read()
    if(touchValueRise<touchThreshold):
        #send the code to the submarine
        SerialPort.write(bytes([codeToGoRight]))
        
    touchValueForward=touch_pin_forward.read()
    if(touchValueRise<touchThreshold):
        #send the code to the submarine
        SerialPort.write(bytes([codeToGoForward]))
        
    touchValueLED=touch_pin_LED.read()
    if(touchValueRise<touchThreshold):
        #send the code to the submarine
        SerialPort.write(bytes([codeToTurnOnLight]))
