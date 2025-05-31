from machine import Pin, ADC
import time


WATER_LEVEL_SENSOR = 15


# Set up ADC for water level sensor
adc = ADC(Pin(WATER_LEVEL_SENSOR))
adc.atten(ADC.ATTN_11DB)  # Read voltage from 0V to 3.6V

# ADC reference voltage and threshold
V_REF = 3.3
THRESHOLD_VOLTAGE = 1.65  # Sensor actuated at ~2.5V, but set a safe threshold

def read_voltage():
    raw_value = adc.read()  # Read ADC value (0-4095)
    return (raw_value / 4095) * V_REF  # Convert to voltage

while True:
    print(read_voltage())
    time.sleep(1)
