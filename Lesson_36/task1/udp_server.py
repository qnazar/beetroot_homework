import socket

HOST = '127.0.0.1'
PORT = 24044

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server:
    server.bind((HOST, PORT))

    data, addr = server.recvfrom(1024)

    print(f'Server received "{data.decode("utf-8")}" from {addr}')

    response = data.decode("utf-8").upper()

    server.sendto(response.encode("utf-8"), addr)



