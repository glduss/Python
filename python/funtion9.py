from machine import Pin
import time

flash = Pin(4, Pin.OUT, value=0)
red = Pin(33, Pin.OUT, value=1)

count = 0

a = 10
b = 1

while a > b:
    
    flash.value(1)
    red.value(0)
    time.sleep_ms(100)
        
        
    flash.value(0)
    red.value(1)
    time.sleep_ms(100)
        
    b += 1
