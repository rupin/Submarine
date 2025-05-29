from machine import Pin, UART, TouchPad
import time

# Initialize UART2 and Direction Control pin
SerialPort = UART(2, baudrate=9600, tx=17, rx=16)  # Adjust TX/RX pins as needed

control_pin = Pin(26, Pin.OUT) 

#Set the control pin direction to Transmit
control_pin.value(1)

touch_pin_sink = TouchPad(Pin(12))
touch_pin_rise = TouchPad(Pin(13))
touch_pin_forward = TouchPad(Pin(15))
touch_pin_right = TouchPad(Pin(4))
touch_pin_left = TouchPad(Pin(14))
touch_pin_light = TouchPad(Pin(27))
codeToSink=192
codeToRise=3
codeToForward=128
codeToRight=8
codeToLeft=64
codeToLight=4


touchThreshold=200
SerialPort.write(bytes([255]))
while(True):
    touchValueSink=touch_pin_sink.read()
    if(touchValueSink<touchThreshold):
        #send the code to the submarine
        SerialPort.write(bytes([codeToSink]))
        

    touchValueRise=touch_pin_rise.read()
    if(touchValueRise<touchThreshold):
        #send the code to the submarine
        SerialPort.write(bytes([codeToRise]))
        
    touchValueForward=touch_pin_forward.read()
    if(touchValueForward<touchThreshold):
        #send the code to the submarine
        SerialPort.write(bytes([codeToForward]))
        
    touchValueRight=touch_pin_right.read()
    if(touchValueRight<touchThreshold):
        #send the code to the submarine
        SerialPort.write(bytes([codeToRight]))
        
    touchValueLeft=touch_pin_left.read()
    if(touchValueLeft<touchThreshold):
        #send the code to the submarine
        SerialPort.write(bytes([codeToLeft]))
        
    touchValueLight=touch_pin_light.read()
    if(touchValueLight<touchThreshold):
        #send the code to the submarine
        SerialPort.write(bytes([codeToLight]))
        
    time.sleep(0.1)
    
