import socket

HOST = '127.0.0.1'
PORT = 8888

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))

    text = input('Enter the text: ')
    key = input('Enter the key: ')
    MSG = text + '&' + key

    client.sendall(MSG.encode())

    response = client.recv(2048)

    print("Your response - ", response.decode())


