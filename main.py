from startiot import Startiot
import pycom
from time import sleep
from machine import Pin
from onewire import DS18X20
from onewire import OneWire

pycom.heartbeat(False)
iot = Startiot()
iot.connect(False)

ow = OneWire(Pin('P9'))
temp = DS18X20(ow)

state = False


while True:
    tmp = temp.read_temp_async()
    print(tmp)
    sleep(1)
    temp.start_convertion()
    iot.send("TEMP,%f" % tmp)
    sleep(30)
