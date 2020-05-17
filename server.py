import pickle
import socket
from _thread import start_new_thread
from player import Player


server = '192.168.0.25'  # My IP address
port = 5555
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    socket.bind((server, port))
except socket.error as e:
    print(e)

socket.listen(2)
print('Waiting for connections, Server started')

player1 = Player(0, 0, 50, 50, (255, 0, 0))
player2 = Player(100, 100, 50, 50, (0, 0, 255))
players = [player1, player2]


def threaded_client(connection, player):
    connection.send(pickle.dumps(players[player]))
    reply = ''
    while True:
        try:
            data = pickle.loads(connection.recv(2048))
            players[player] = data

            if not data:
                print('Disconnected')
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]

                print(f'Received: {data}')
                print(f'Sending: {reply}')

            connection.sendall(pickle.dumps(reply))
        except Exception as e:
            print(e)
            break

    print('Lost connection')
    connection.close()


current_player = 0

while True:
    connection, address = socket.accept()
    print(f'Connected to: {address}')

    start_new_thread(threaded_client, (connection, current_player))
    current_player += 1
