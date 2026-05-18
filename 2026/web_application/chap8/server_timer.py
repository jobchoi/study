import socket
import time
import threading

# setup server socket
HOST = ''
PORT = 5600
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

clients = [] 
clients_lock = threading.Lock() 

print(f"⏰ 시간 브로드캐스트 서버 가동 중... (Port: {PORT})")


# =========================================================================
# [1] 진짜 콜백 함수 정의 (타이머 인터럽트가 발생했을 때 '실행할 작업')
# =========================================================================
def send_time_callback():
    """1초 타이머가 터졌을 때 호출될 실제 작업(Callback)"""
    current_time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    
    with clients_lock:
        for client in clients[:]:
            try:
                client.send(current_time_str.encode())
            except Exception as e:
                print(f"⚠️ 클라이언트에 시간 전송 실패 (연결 끊김): {e}")
                if client in clients:
                    clients.remove(client)
                client.close()


# =========================================================================
# [2] 타이머 인터럽트 엔진 (콜백 함수를 인자로 받음)
# =========================================================================
def time_interrupt_handler(callback):
    """1초마다 인터럽트를 발생시키고, 넘겨받은 콜백 함수를 실행하는 핸들러"""
    # 1. 인터럽트가 발생했으니, 등록된 콜백 함수를 실행해라!
    callback()

    # 2. 다음 1초 뒤 인터럽트가 발생하면 또 이 콜백을 실행하도록 재귀 예약
    t = threading.Timer(1.0, time_interrupt_handler, args=[callback])
    t.daemon = True
    t.start()


# 최초 1회 인터럽트 핸들러 실행 (콜백 함수를 인자로 전달!)
time_interrupt_handler(send_time_callback)
# =========================================================================


# [메인 루프] 오직 클라이언트 접속만 체크 (인터럽트와 완전 분리)
try:
    while True:
        client_socket, addr = server_socket.accept()
        print(f"👤 클라이언트 접속: {addr}")
        
        with clients_lock:
            clients.append(client_socket)

except KeyboardInterrupt:
    print("\n⏹️ 서버 종료 중...")
finally:
    server_socket.close()
