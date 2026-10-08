from machine import Pin
import time

flash = Pin(4, Pin.OUT, value=0)
red = Pin(33, Pin.OUT, value=1)

count = 0

while True:
    
    count += 1
    
    if count % 3 == 0:
        flash.value(1)
        red.value(0)
        time.sleep_ms(500)
        
        
        flash.value(0)
        red.value(1)
        time.sleep_ms(500)
        
    else:
        
        flash.value(1)
        time.sleep_ms(500)
        
        flash.value(0)
        time.sleep_ms(500)
