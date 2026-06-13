import socket
import threading 

def handler(sock):
    while True:
        try:
            msg, addr = sock.recvfrom(1024)
        except:
            continue
        else :
            print(msg.decode())

conn = ("localhost", 2500)
svr = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

my_id = input("Enter your ID: ")
cThread = threading.Thread(target=handler, args=(svr,))
cThread.daemon = True
cThread.start()
while True:
    msg = "["+my_id+"] " + input()
    svr.sendto((my_id + ": " + msg).encode(), conn)