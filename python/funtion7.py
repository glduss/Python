from machine import Pin

flash = Pin(4, Pin.OUT, value=0)
red = Pin(33, Pin.OUT, value=1)

leds = [flash, red]
print(len(leds))

leds[0].value(1)
leds[1].value(0)

