import socket

# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# sock.connect(('localhost', 5000))

# print(f"client 2 - 현재 시간 : {sock.recv(1024).decode()}")

# sock.close()

PORT = 5600

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', PORT))

print("📡서버로부터 시간을 수신합니다. - client 2")

try:
    while True:
        data = sock.recv(1024)
        if not data:
            print(f"서버와의 연결이 종료되었습니다.{data.decode()}", end='')
            break
        else:
            print(f"서버로부터 수신된 시간: {data.decode()}")
except: 
    pass
finally:
    sock.close()