from machine import Pin
import time

ON = True
OFF = False

def blink_once(times, pin_no, ms_on, ms_off):
    flash = Pin(pin_no, Pin.OUT, value=0)
    for i in range(times):
        if pin_no == 4:
            flash.value(ON)
            time.sleep_ms(ms_on)
            flash.value(OFF)
            time.sleep_ms(ms_off)
        else:
            flash.value(OFF)
            time.sleep_ms(ms_on)
            flash.value(ON)
            time.sleep_ms(ms_off)
        
blink_once(3, 4, 300, 500)
blink_once(10, 33, 300, 100)