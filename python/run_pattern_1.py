from machine import Pin
import time

flash = Pin(4, Pin.OUT, value=0)
red = Pin(33, Pin.OUT, value=1)

slow = [800, 800, 800]
fast = [100, 100, 100, 100, 100, 100]

#for ms in slow:
#    flash.value(1)
#    time.sleep_ms(ms)
#    flash.value(0)
#    time.sleep_ms(200)
    
#for ms in fast:
#    flash.value(1)
#    time.sleep_ms(ms)
#    flash.value(0)
#    time.sleep_ms(200)

def run_pattern(pin_obj, pattern_list):
    for ms in pattern_list:
        if pin_obj == flash:
            pin_obj.value(1)
            time.sleep_ms(ms)
            pin_obj.value(0)
            time.sleep_ms(200)
        else:
            pin_obj.value(0)
            time.sleep_ms(ms)
            pin_obj.value(1)
            time.sleep_ms(200)
        
run_pattern(flash, fast)
run_pattern(red, slow)
    