import socket

BUFSIZE = 1024
PORT = 2000
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

svrIP = input(("Server IP :(default : 127.0.0.1) : "))
if svrIP == '':
    svrIP = '127.0.0.1'

port = input(f"port(default : {PORT}) : ")
if port == '':
    port = PORT
else:
    port = int(port)

sock.connect((svrIP, port))
print(f"Connected to {svrIP}")

while True:
    msg = input("send msg : ")

    if not msg :
        continue
    try:
        sock.send(msg.encode())

    except:
        print("연결이 종료됨")
        break


    try:
        msg = sock.recv(BUFSIZE)
        if not msg:
            print("연결이 종료됨")
            break
        print(f"received msg : {msg.decode()}")

    except:
        print("연결이 종료됨")
        break

sock.close()