from machine import Pin, UART, TouchPad, ADC
import time

#relay pins
sink_valve=4
sink_pump=2

rise_valve=12
rise_pump=13

forward_thruster=14
left_thruster=27

right_thruster=32
led_pin=33

tank_empty_probe=25
tank_full_probe=15





#actioncodes
sink_code=192
rise_code=3
forward_code=8
left_code=16
right_code=32
led_code=4

off_code=0








# Initialize UART2 and Direction Control pin
SerialPort = UART(2, baudrate=9600, tx=17, rx=16)  # Adjust TX/RX pins as needed

control_pin = Pin(26, Pin.OUT) 

#Set the control pin direction to Transmit
control_pin.value(0)

sinkv=Pin(sink_valve, Pin.OUT)
sinkp=Pin(sink_pump, Pin.OUT)

risev=Pin(rise_valve, Pin.OUT)
risep=Pin(rise_pump, Pin.OUT)

forward=Pin(forward_thruster, Pin.OUT)
left=Pin(left_thruster, Pin.OUT)

right=Pin(right_thruster, Pin.OUT)
left=Pin(left_thruster, Pin.OUT)

led=Pin(led_pin, Pin.OUT)

# Set up ADC for water level sensor
tank_empty = ADC(Pin(tank_empty_probe))
tank_empty.atten(ADC.ATTN_11DB)


# Set up ADC for water level sensor
tank_full = ADC(Pin(tank_full_probe))
tank_full.atten(ADC.ATTN_11DB)




while(True):
    if SerialPort.any():
        data=SerialPort.read()
        recievedCommand=ord(data)
        print(recievedCommand)
        
        tank_full_signal = tank_full.read()
        tank_empty_signal = tank_empty.read() 
        
        if(recievedCommand==sink_code):
            
            sinkv.value(1)
            sinkp.value(1)
            
            
            
            led.value(0)
            right.value(0)
            left.value(0)
            forward.value(0)
            
            risev.value(0)
            risep.value(0)
            
        if(recievedCommand==rise_code):
            risev.value(1)
            risep.value(1)
            
            led.value(0)
            right.value(0)
            left.value(0)
            forward.value(0)
            sinkv.value(0)
            sinkp.value(0)
            
            
        if(recievedCommand==forward_code):
            forward.value(1)
            
            led.value(0)
            right.value(0)
            left.value(0)            
            sinkv.value(0)
            sinkp.value(0)
            risev.value(0)
            risep.value(0)
            
        if(recievedCommand==left_code):
            left.value(1)
            led.value(0)
            right.value(0)
            forward.value(0)
            sinkv.value(0)
            sinkp.value(0)
            risev.value(0)
            risep.value(0)
            
        if(recievedCommand==right_code):
            right.value(1)
            
            led.value(0)            
            left.value(0)
            forward.value(0)
            sinkv.value(0)
            sinkp.value(0)
            risev.value(0)
            risep.value(0)
            
        if(recievedCommand==led_code):
            led.value(1)
            
            right.value(0)
            left.value(0)
            forward.value(0)
            sinkv.value(0)
            sinkp.value(0)
            risev.value(0)
            risep.value(0)
            
        if(recievedCommand==off_code):
            led.value(0)
            right.value(0)
            left.value(0)
            forward.value(0)
            sinkv.value(0)
            sinkp.value(0)
            risev.value(0)
            risep.value(0)
            
        
        
    

