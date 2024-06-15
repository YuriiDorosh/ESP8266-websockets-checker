import network

def connect_wifi(ssid: str, password: str):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while not wlan.isconnected():
        pass
    print('Connection successful')
    print(wlan.ifconfig())
