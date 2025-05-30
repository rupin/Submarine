from machine import Pin, UART, TouchPad
import time

#touchinputs
sink=4
rise=12
forward=13
left=14
right=15
led=27

#actioncode
sink_code=192
rise_code=3
forward_code=8
left_code=4
right_code=16
led_code=32

off_code=0

# initialise the toucinputs

rise_touch=TouchPad(Pin(rise))
sink_touch=TouchPad(Pin(sink))
forward_touch=TouchPad(Pin(forward))
left_touch=TouchPad(Pin(left))
right_touch=TouchPad(Pin(right))
led_touch=TouchPad(Pin(led))

threshold=200
# Initialize UART2 and Direction Control pin
SerialPort = UART(2, baudrate=9600, tx=17, rx=16)  # Adjust TX/RX pins as needed

control_pin = Pin(26, Pin.OUT) 

#Set the control pin direction to Transmit
control_pin.value(1)

while(True):
    time.sleep(0.5)
    
    sink_touch_value=sink_touch.read()
    if(sink_touch<threshold): # means someone touch the pin
        SerialPort.write(bytes([sink_code]))
        continue
        
    rise_touch_value=rise_touch.read()
    if(rise_touch_value<threshold): # means someone touch the pin
        SerialPort.write(bytes([rise_code]))
        continue
    
    fwd_touch_value=forward_touch.read()
    if(fwd_touch_value<threshold): # means someone touch the pin
        SerialPort.write(bytes([forward_code]))
        continue
        
    left_touch_value=left_touch.read()
    if(left_touch_value<threshold): # means someone touch the pin
        SerialPort.write(bytes([left_code]))
        continue
    
    right_touch_value=right_touch.read()
    if(right_touch_value<threshold): # means someone touch the pin
        SerialPort.write(bytes([right_code]))
        continue
    
    led_touch_value=led_touch.read()
    if(led_touch_value<threshold): # means someone touch the pin
        SerialPort.write(bytes([led_code]))
        continue
    
    
    SerialPort.write(bytes([off_code]))


