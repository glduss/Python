from machine import Pin
import time

flash = Pin(4, Pin.OUT, value=0)

for i in range(3):
    flash.value(1)
    time.sleep_ms(300)
    flash.value(0)
    time.sleep_ms(300)