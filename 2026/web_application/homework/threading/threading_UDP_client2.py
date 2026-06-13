import socket
import threading

BUFSIZE = 1024

def handler(sock):
    while True:
        try:
            msg, addr = sock.recvfrom(BUFSIZE)
        except:
            continue
        else:
            print(msg.decode())