from machine import Pin, PWM, SPI
import time
from RFID.mfrc522 import MFRC522

sck = Pin(18, Pin.OUT)
mosi = Pin(23, Pin.OUT)
miso = Pin(19, Pin.OUT)
spi = SPI(baudrate=100000, polarity=0, phase=0, sck=sck, mosi=mosi, miso=miso)
p0 = Pin(21, Pin.OUT)
sda = Pin(5, Pin.OUT)

def start():
    p0.on()
    while True:
        rdr = MFRC522(spi, sda)
        uid = ""
        (stat, tag_type) = rdr.request(rdr.REQIDL)
        if stat == rdr.OK:
            (stat, raw_uid) = rdr.anticoll()
            if stat == rdr.OK:
                p0.off()
                time.sleep(5)
                p0.on()
