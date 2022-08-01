import socket

HOST = '127.0.0.1'
PORT = 24044

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client:
    client.sendto(b'Hello', (HOST, PORT))
    data, addr = client.recvfrom(1024)
    print(f"Client got response '{data.decode('utf-8')}' from server {addr}")

