# Echo server program
import socket
import pickle

HOST = ''  # Symbolic name meaning all available interfaces
PORT = 50007  # Arbitrary non-privileged port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((HOST, PORT))
    sock.listen()
    conn, addr = sock.accept()

    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            # data = pickle.loads(conn.recv(1024))

            if not data:
                break
            print(data)
            conn.sendall(data)
            # conn.sendall(pickle.dumps(data))
