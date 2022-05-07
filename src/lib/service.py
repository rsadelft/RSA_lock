from machine import Pin, PWM
import time
def start():
    print("123456789123456789")
    p0 = Pin(21, Pin.OUT)
    p1 = PWM(Pin(15))
    p0.off()
    p1.freq(500)
    p1.duty(512)
    time.sleep(5)
    p0.on()
    p1.deinit()