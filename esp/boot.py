import config
from wifi import connect_wifi
from websocket_client import websocket_connect, send_ping

def main():
    connect_wifi(config.SSID, config.PASSWORD)
    websocket = websocket_connect(config.WS_HOST, config.WS_PORT, config.WS_PATH)
    send_ping(websocket)

if __name__ == '__main__':
    main()
