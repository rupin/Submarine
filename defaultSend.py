from machine import Pin, UART

import time
defaultData=55

# Initialize UART2 and Direction Control pin
SerialPort = UART(2, baudrate=9600, tx=17, rx=16)  # Adjust TX/RX pins as needed

control_pin = Pin(26, Pin.OUT) 

#Set the control pin direction to Transmit
control_pin.value(1)

while(True):
    SerialPort.write(bytes([defaultData]))
    time.sleep(1)