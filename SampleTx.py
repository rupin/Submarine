from machine import Pin, UART, TouchPad

# Initialize UART2 and Direction Control pin
SerialPort = UART(2, baudrate=9600, tx=17, rx=16)  # Adjust TX/RX pins as needed

control_pin = Pin(26, Pin.OUT) 

#Set the control pin direction to Transmit
control_pin.value(1)

touch_pin_sink = TouchPad(Pin(4))
touch_pin_rise = TouchPad(Pin(15))
codeToSink=192
codeToRise=3

touchThreshold=700

while(True):
    touchValueSink=touch_pin_sink.read()
    if(touchValueSink<touchThreshold):
        #send the code to the submarine
        SerialPort.write(bytes([codeToSink]))
        

    touchValueRise=touch_pin_rise.read()
    if(touchValueRise<touchThreshold):
        #send the code to the submarine
        SerialPort.write(bytes([codeToRise]))
    
