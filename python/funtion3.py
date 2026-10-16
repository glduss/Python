from machine import Pin
import time

flash = 4

def blink_once(pin_no, times, ms_on, ms_off):
    
    if pin_no == flash:
        ON = True
        OFF = False
    else:
        ON = False
        OFF = True
        
    led_controller = Pin(pin_no, Pin.OUT, value=0)
    
    for i in range(times):
            led_controller.value(ON)
            time.sleep_ms(ms_on)
            led_controller.value(OFF)
            time.sleep_ms(ms_off)
        
        
blink_once(flash, 3, 300, 500)

blink_once(33, 10, 300, 100)
