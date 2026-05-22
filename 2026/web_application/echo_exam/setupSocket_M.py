from socket import *


def setUp_server(port, ubufsize):
    PORT = 2000
    BUFSIZE = 1024

    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(('', port))
    sock.listen(5)
    print("Waiting for clients")