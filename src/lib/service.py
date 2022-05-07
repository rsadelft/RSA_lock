from machine import Pin, SPI
import time
def start():
    print("123456789123456789")
    p0 = Pin(21, Pin.OUT)
    p0.on()
    time.sleep(1)
    p0.off()