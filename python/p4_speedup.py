from machine import Pin
import time

flash = Pin(4, Pin.OUT, value=0)

speeds = []
for i in range(6):
    speeds.append(600 - i * 100)
print(speeds)

for ms in speeds:
    flash.value(1)
    time.sleep_ms(ms)
    flash.value(0)
    time.sleep_ms(ms)