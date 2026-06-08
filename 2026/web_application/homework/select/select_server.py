
# select
import socket, select

sock_list = []
BUFFER = 1024
PORT = 2500

s_sock = socket.socket() # TCP 소켓
s_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
s_sock.listen(5)

sock_list.append(s_sock) # 서버 소켓을 목록에 추가
print("Server waiting on Port "+str(PORT))

while True:
    r_sock, w_sock, e_sock = select.select(sock_list,[],[],0) # 감시설정

    for s in r_sock:    # 읽기 이벤트 소켓 조사
        if s == s_sock: # 서버소켓인가?
            c_sock, addr = s_sock.accept()
            sock_list.append(c_sock)
            print("Client(%s %s) connect" %addr)

        else:
            try:
                data = s.recv(BUFFER)
                print("Recevied : ", data.decode())
                if(data):
                    s.send(data)
            except : # 연결종료됨2                
                print("client (%s    %s) is offline "%addr)
                s.close()
                sock_list.remove(s)
                continue
    s_sock.close()

            
