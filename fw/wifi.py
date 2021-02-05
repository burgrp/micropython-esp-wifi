from machine import Timer
from machine import Pin

def init():
    pin = Pin(2, Pin.OUT)

    pin.off()

    state = False

    def tick():
        nonlocal state
        state = not state
        #print("tick")
        pin.value(state)


    tim = Timer(-1)
    tim.init(period=500, mode=Timer.PERIODIC, callback = lambda t: tick())





#     print("Configuring WiFi...")

#     import network
    
#     wlan = network.WLAN(network.STA_IF)
#     wlan.active(True)
    
#     if not wlan.isconnected():
#         print("Connecting to WiFi...")
#         wlan.connect("416T", "ferdamravenec")

#     while not wlan.isconnected():
#         pass
#     print('network config:', wlan.ifconfig())




# >>> tim = Timer(-1)
# tim = Timer(-1)
# >>> tim.init(period=2000, mode=Timer.PERIODIC, callback=lambda t:print(2))

