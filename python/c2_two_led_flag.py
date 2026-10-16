from machine import Pin
import time

flash = Pin(4, Pin.OUT, value = 0)
red = Pin(33, Pin.OUT, value = 1)

counter = 0
red_on = 0

while True:
    flash.value(1)
    
    if (red_on == 1):
        red.value(0)
        
    time.sleep_ms(100)
    
    flash.value(0)
    
    if (red_on == 1):
        red.value(1)
        red_on = 0
        
    time.sleep_ms(100)
    
    counter += 1
    
    if counter > 2:
        counter = 0
        red_on = 1