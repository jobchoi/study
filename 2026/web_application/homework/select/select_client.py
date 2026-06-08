from socket import *
from select import * 

socks = []

BUFSIZE = 1024

sock = socket()
sock.setsockopt(SOL_SOCKET, SO_REUSEADDR,1)
socks.append(sock)
sock.connect(('localhost',2500)) # 서버 연결

while True:
    r_sock, w_sock, e_sock = select(socks,[],[],0)
    if r_sock:
        for s in r_sock:
            if s == sock :
                msg = sock.recv(BUFSIZE).decode()
                print(f"수신 메시지 : {msg}")
    smsg = input("전송메세지 : ")
    sock.send(smsg.encode())