import socket
import time 

host = ''
PORT = 2500
BUFSIZE = 1024

clients = []

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host,PORT))
s.setblocking(0)

print('Server Startted')

while True:
    try:
        data, addr = s.recvfrom(BUFSIZE)
        if "quit" in data.decode():
            clients.remove(addr)
            print(f"{addr}")
        if addr not in clients:
            print("new client")
            clients.append(addr)
        print(time.ctime(time.time()) + str(addr) + '::'+data.decode())
        for client in clients:
            if client != addr:
                s.sendto(data,client)
    except:
        pass
s.close()
