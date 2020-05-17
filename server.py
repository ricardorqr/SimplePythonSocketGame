import socket
from _thread import *
import sys

server = '192.168.0.25'  # My IP address
port = 5555
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    socket.bind((server, port))
except socket.error as e:
    print(e)

socket.listen(2)
print('Waiting for connections, Server started')


def read_position(string):
    string = string.split(',')
    return int(string[0]), int(string[1])


def make_position(tuple):
    return str(tuple[0]) + ',' + str(tuple[1])


positions = [(0, 0), (100, 100)]


def threaded_client(connection, player):
    connection.send(str.encode(make_position(positions[player])))
    reply = ''
    while True:
        try:
            data = read_position(connection.recv(2048).decode())
            positions[player] = data

            if not data:
                print('Disconnected')
                break
            else:
                if player == 1:
                    reply = positions[0]
                else:
                    reply = positions[1]

                print(f'Received: {data}')
                print(f'Sending: {reply}')

            connection.sendall(str.encode(make_position(reply)))
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
