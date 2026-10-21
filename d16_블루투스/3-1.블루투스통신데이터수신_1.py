from machine import Pin, PWM
import bluetooth,ble_simple_peripheral,time

ble = bluetooth.BLE()
p = ble_simple_peripheral.BLESimplePeripheral(ble,name='pyD_3749')

key = Pin(0, Pin.IN, Pin.PULL_UP)
prev_key = key.value() 

M1_motor = PWM(Pin(4), freq = 10000 ,duty=0)
M2_motor = PWM(Pin(5), freq = 10000 ,duty=0)
M3_motor = PWM(Pin(40), freq = 10000 ,duty=0)
M4_motor = PWM(Pin(41), freq = 10000 ,duty=0)


def on_rx(read):
    print("RX", read)


p.on_write(on_rx)

try:
    while True:
        curr_key = key.value()
        if curr_key != prev_key:
            prev_key = curr_key
            if curr_key == 0:
                M1_motor.duty(100)
                M2_motor.duty(100)
                M3_motor.duty(100)
                M4_motor.duty(100)
                print("100")
                time.sleep(1)
            
            else:
                M1_motor.duty(0)
                M2_motor.duty(0)
                M3_motor.duty(0)
                M4_motor.duty(0)
                print("0")
                time.sleep(3)
        

except KeyboardInterrupt:
    M1_motor.deinit()
    M2_motor.deinit()
    M3_motor.deinit()
    M4_motor.deinit()
    print("코드를 종료합니다.")