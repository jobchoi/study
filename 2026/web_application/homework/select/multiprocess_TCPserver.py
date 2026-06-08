# EX_multiprocess
from socket import *
from multiprocessing import Process


BUFSIZE = 1024
PORT = 2500

def handle(sock):
    while True:
        msg = sock.recv(BUFSIZE)
        print(f"Received message : {msg.decode()}")
        sock.send(msg)

if __name__ == "__main__":
    sock = socket()
    addr = ('',PORT)
    sock.listen(4)

    while True:
        c_sock, r_addr = sock.accept()
        print(f"====> {r_addr} is connected")
        p1 = Process(target=handle,args=(c_sock))
        p1.start()

