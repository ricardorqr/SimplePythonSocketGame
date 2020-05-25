# Echo client program
import socket
import pickle

HOST = '192.168.0.25'  # The remote host
PORT = 50007            # The same port as used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    # sock.sendall(pickle.dumps("Hello World"))
    # data = pickle.loads(sock.recv(1024))
    sock.sendall(b"Hello World")
    data = sock.recv(1024)

print(f'Received: {data}')
