import ctypes
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 5000))

def sendMessage(msg):
    ctypes.windll.user32.MessageBoxW(0, msg, "Message", 0)

server.listen(5)
while True:
    try:
        client, addr = server.accept()
        message = client.recv(1024).decode()

        print(message)
        sendMessage(message)

    except KeyboardInterrupt:
        break

server.close()