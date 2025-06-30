import ctypes
import socket
import os

os.system("pip install requests")


import requests

requests.post("http://192.168.0.219:5555", data= socket.gethostbyname("localhost"))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 5000))

def sendMessage(msg):
    ctypes.windll.user32.MessageBoxW(0, msg, "Message", 0)

server.listen(5)
while True:
    try:
        client, addr = server.accept()
        message = client.recv(1024).decode()

        sendMessage(message)

    except KeyboardInterrupt:
        break

server.close()
