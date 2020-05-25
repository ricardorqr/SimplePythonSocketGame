import socket
from _thread import start_new_thread
from player import Player
import pickle


current_player = 0
IP = ""
PORT = 5555

try:
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.bind((IP, PORT))
    socket.listen()
except Exception as e:
    str(e)

print("Waiting for a connection, Server Started")

player1 = Player(0, 0, 50, 50, (255, 0, 0))
player2 = Player(0, 0, 50, 50, (0, 0, 255))
players = [player1, player2]


def thread_client(conn, player):
    conn.send(pickle.dumps(players[player]))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]

                print("Received: ", data)
                print("Sending : ", reply)

            conn.sendall(pickle.dumps(reply))
        except Exception as e:
            str(e)
            break

    print("Lost connection")
    conn.close()


while True:
    connection, address = socket.accept()
    print("Connected to:", address)

    start_new_thread(thread_client, (connection, current_player))
    current_player += 1
