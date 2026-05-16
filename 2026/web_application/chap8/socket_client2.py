import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(('localhost', 5000))

print(f"client 2 - 현재 시간 : {sock.recv(1024).decode()}")

sock.close()