import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket.connect(('localhost',5000))
sock.connect(('127.0.0.1', 5500))

while True: 
    print(f"현재시간 : {sock.recv(1024).decode()}")

sock.close()