import usocket
import ubinascii
import time
import machine

def websocket_connect(host: str, port: int, path: str):
    addr_info = usocket.getaddrinfo(host, port)
    addr = addr_info[0][-1]
    s = usocket.socket()
    s.connect(addr)
    websocket_key = ubinascii.b2a_base64(machine.rng().to_bytes(16, 'little')).decode().strip()
    s.send(b'GET {} HTTP/1.1\r\n'.format(path) +
           b'Host: {}:{}\r\n'.format(host, port) +
           b'Connection: Upgrade\r\n' +
           b'Upgrade: websocket\r\n' +
           b'Sec-WebSocket-Version: 13\r\n' +
           b'Sec-WebSocket-Key: {}\r\n\r\n'.format(websocket_key))
    return s

def send_ping(s):
    while True:
        s.send(b'ping')
        time.sleep(5)
