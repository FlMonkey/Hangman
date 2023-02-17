import socket

HOST = '127.0.0.1'  # IP address of peer A
PORT = 8080        # same port number used by peer A

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, peer A')
    data = s.recv(1024)

print('Received', repr(data))
