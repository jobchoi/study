import socket
import time
import select   

# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
# address = (('localhost', 5000))

# sock.bind(address)    
# sock.listen(5)

# inputs = [sock]

# while True:

#     # print("클라이언트의 접속을 기다리는 중...")
#     # client_sock, addr = sock.accept()
#     # print(f"클라이언트가 접속했습니다. (주소: {addr})")

#     # current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
#     # client_sock.send(current_time.encode())

#     # client_sock.close()

# setup server socket
HOST = ''
PORT = 5600
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

# list of sockets to monitor for incoming connections
readsocks = [server_socket]
cleients = [] # 클라이언트 소켓 리스트

print(f"⏰ 시간 브로드캐스트 서버 가동 중... (Port: {PORT})")
last_send_time = time.time()

try:
    while True:
        # check for incoming connections or data
        readable, _, _ = select.select(readsocks, [], [], 0.1) 

        for sock in readable:
            if sock is server_socket:
                # new client connection
                client_socket, addr = server_socket.accept()
                print(f"👤 클라이언트 접속: {addr}")
                readsocks.append(client_socket)
                cleients.append(client_socket)
            else:
                # existing client sent data (or disconnected)
                data = sock.recv(1024)
                if not data:
                    # client disconnected
                    print(f"👤 클라이언트 접속 종료: {sock.getpeername()}")
                    readsocks.remove(sock)
                    cleients.remove(sock)
                    sock.close()

        current_time = time.time()

        if current_time - last_send_time >= 1:
            # send current time to all clients every second
            current_time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            for client in cleients:
                try:
                    client.send(current_time_str.encode())
                except Exception as e:
                    print(f"⚠️ 클라이언트에 시간 전송 실패: {e}")
                    readsocks.remove(client)
                    cleients.remove(client)
                    client.close()
            last_send_time = current_time

except KeyboardInterrupt:
    print("\n⏹️ 서버 종료 중...")