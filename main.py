import time
import machine
from machine import Pin

adc = machine.ADC(bits=10)
#Important that this pin is the same one as the sensor is conected to
tempPin = adc.channel(pin='P16')

while True:
    millivolts = tempPin.voltage()
    celsius = (millivolts - 500.0) / 10.0

    print("Tempature = {}".format(celsius))
    
    #Send every 20 minutes
    time.sleep(1200)