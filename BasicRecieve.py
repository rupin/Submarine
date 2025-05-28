from machine import Pin, UART

import time

# Initialize UART2 and Direction Control pin
SerialPort = UART(2, baudrate=9600, tx=17, rx=16)  # Adjust TX/RX pins as needed
control_pin = Pin(26, Pin.OUT)

control_pin.value(0)  # Set direction to receive

while (True):
    #print("Checking")
    if SerialPort.any():
        data=SerialPort.read()
        print(ord(data))
    
