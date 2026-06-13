import  socket
import time

HOST = ''
PORT = 2500
BUFFER_SIZE = 1024  

clients = []

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))
s.setblocking(False)

print("Server Started...")

while True:
    try:
        data, addr = s.recvfrom(BUFFER_SIZE)
        # print("====> : ", s.recvfrom(BUFFER_SIZE))

        if "quit" in data.decode():
            s.close()   
        if addr in clients:
            clients.remove(addr)
            print(f"==> {addr} is lost.")
        if addr not in clients :
            print(f"new client {addr} is connected.")
            clients.append(addr)
        print(time.ctime(time.time()) + str(addr) + ':'+ data.decode())
        for client in clients:
            if client != addr:
                s.sendto(data, client)
    except :
        pass
s.close()   