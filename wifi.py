from machine import Timer
from machine import Pin
import network


def init(ssid, password, ledPin=2, ledLogic=False):

    pin = Pin(ledPin, Pin.OUT)

    connectionState = False

    def check():
        connected = wlan.isconnected()

        nonlocal connectionState
        if connected != connectionState:
            connectionState = connected
            if connected:
                print("WiFi connected, IP:", wlan.ifconfig()[0])
                pin.value(ledLogic)

        if not connected:
            pin.value(not pin.value())
            if wlan.status() != network.STAT_CONNECTING:
                print("Connecting to WiFi...")
                wlan.connect(ssid, password)

    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    tim = Timer(-1)
    tim.init(period=100, mode=Timer.PERIODIC, callback=lambda t: check())


