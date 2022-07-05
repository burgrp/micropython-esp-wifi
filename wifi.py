from machine import Timer
from machine import Pin
import network


def init(ssid, password, ledPin=2, ledLogic=True):

    pin = Pin(ledPin, Pin.OUT)

    pin.off()

    ledState = False
    connectionState = False

    def tick():
        connected = wlan.isconnected()

        nonlocal ledState
        ledState = (not connected and not ledState)
        pin.value(ledState == ledLogic)

        nonlocal connectionState
        if connected != connectionState:
            connectionState = connected
            if connected:
                print("WiFi connected, IP:", wlan.ifconfig()[0])
            else:
                print("WiFi disconnected") 


    tim = Timer(-1)
    tim.init(period=100, mode=Timer.PERIODIC, callback=lambda t: tick())

    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    print("Connecting to WiFi...")
    wlan.connect(ssid, password)

