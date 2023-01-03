from machine import Pin
import network
import virtual_timer
from machine import Timer


def init(ssid=None, password=None, ledPin=2, ledLogic=False):

    pin = Pin(ledPin, Pin.OUT)
    pin.value(ledLogic)

    connectionState = False

    def check(timer):
        connected = wlan.isconnected()

        nonlocal connectionState
        if connected != connectionState:
            connectionState = connected
            if connected:
                print('WiFi connected, IP:', wlan.ifconfig()[0])
                pin.value(ledLogic)
            if not connected:
                print('WiFi disconnected')

        if not connected:
            pin.value(not pin.value())
            if wlan.status() != network.STAT_CONNECTING:
                print('Connecting to WiFi SSID:', ssid)
                wlan.connect(ssid, password)

    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    virtual_timer.VirtualTimer().init(period=500, mode=Timer.PERIODIC, callback=check)

