from socket import *
from threading import *

class MultiChatServer:

    # 소켓 생성, 연결후 accept_client() 호출
    def __init__(self):
        self.clients = []
        self.final_received_message =""
        self.s_sock = socket(AF_INET, SOCK_STREAM)
        self.ip=''
        self.port=2500
        self.s_sock.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        self.s_sock.bind((self.ip, self.port))
        print("클라이언트 대기중...")
        self.s_sock.listen(100)
        self.accept_client()

    def accept_client(self):
        while True:
            client = c_socket, (ip,port) = self.s_sock.accept()
            if client not in self.clients:
                self.clients.append(client) #접속된 소켓목록에 추가
            print(ip, ":",str(port),'가 연결되었습니다')
            # Thread - 수신
            cth = Thread(target=self.receive_message, args=(c_socket,))
            # Thread 시작
            cth.start()

    # 데이터 수시느 모든 클라이언트에 전송.
    def receive_message(self, c_socket):
        while True:
            try:
                incoming_message = c_socket.recv(256)
                # 연결이 종료
                if not incoming_message: 
                    break
            except:
                continue
            else:
                self.final_received_message = incoming_message.decode('utf-8')
                print(self.final_received_message)
                self.send_all_clients(c_socket)
        c_socket.close()


    # 송신 클라이언트 외에 메시지 전송
    def send_all_clients(self, senders_socket):
        # 목록에 있는 모든 소켓
        for client in self.clients:
            socket, (ip, port) = client
            # 송신 클라이언트는 제외
            if socket is not senders_socket:
                try: 
                    socket.sendall(self.final_received_message.encode())
                except: # 연결종료
                    # 소켓 제거
                    self.clients.remove(client)
                    print("{},{} 연결이 종료되었습니다.".format(ip,port))
    

if __name__ == "__main__":
    MultiChatServer()

