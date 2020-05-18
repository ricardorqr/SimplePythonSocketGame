import socket
import pickle


HOST, PORT = "192.168.0.25", 9999
data = "Test Rico"

# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    sock.sendall(pickle.dumps(bytes(data + "\n", "utf-8")))

    # Receive data from the server and shut down
    received = str(pickle.loads(sock.recv(1024)), "utf-8")

print("Sent:     {}".format(data))
print("Received: {}".format(received))
