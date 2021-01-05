# This file is executed on every boot (including wake-boot from deepsleep)

# notify
print('RUN: boot.py')

import time
from umqttsimple import MQTTClient
import ubinascii
import machine
import micropython
import network
import esp

# Set the debug to None and activate the garbage collector
esp.osdebug(None)
import gc
gc.collect()

# Network credetntials
ssid = 'fddb6a'
password = 'bride.018.unity'

def do_connect(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())

do_connect(ssid, password)