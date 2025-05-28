from machine import Pin, TouchPad
import time

touch_pin = TouchPad(Pin(4))

touchThreshold=700

while(True):
    touchValue=touch_pin.read()
    if(touchValue<touchThreshold):
        print("Touch Detected")
    else:
        print("Touch Not Detected")
    time.sleep(0.1)
