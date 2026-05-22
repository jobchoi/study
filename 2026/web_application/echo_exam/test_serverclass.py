from socket import *


class EchoServer:
    def __init__(self, port, ubufsize):
        self.PORT = port
        self.BUFSIZE = ubufsize

    def setUp_server(self):
        sock = socket(AF_INET, SOCK_STREAM)
        sock.bind(('', self.PORT))
        sock.listen(5)
        print("Waiting for clients")
        return sock 
    