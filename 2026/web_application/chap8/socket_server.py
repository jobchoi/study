import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
address = (('localhost', 5000))

sock.bind(address)    
sock.listen(5)


while True:
    print("클라이언트의 접속을 기다리는 중...")
    client_sock, addr = sock.accept()
    print(f"클라이언트가 접속했습니다. (주소: {addr})")

    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    client_sock.send(current_time.encode())

    client_sock.close()