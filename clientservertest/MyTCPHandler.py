import socketserver
import pickle


class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = pickle.loads(self.request.recv(1024).strip())
        print(f"self.client_address: {self.client_address}")
        print(f"{self.client_address[0]} wrote: {self.data}")
        # just send back the same data, but upper-cased
        self.request.sendall(pickle.dumps(self.data.upper()))


if __name__ == "__main__":
    HOST, PORT = "", 9999

    # Create the server, binding to 192.168.0.25 on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()
