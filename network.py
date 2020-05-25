import socket
import pickle


class Network:

    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = '192.168.0.12'  # My internal IP
        self.port = 5555
        self.address = (self.server, self.port)
        self.player = self.connect()

    def get_player(self):
        return self.player

    def connect(self):
        try:
            self.client.connect(self.address)
            return pickle.loads(self.client.recv(2048))
        except Exception as e:
            print(e)

    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048))
        except Exception as e:
            print(e)
