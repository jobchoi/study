import socket
import threading


def handler(c, a):  # 💡 매개변수 'a'가 바로 클라이언트의 (IP, Port) 주소 튜플
    global connections
    print(f"✨ [연결 성공] 클라이언트 주소: {a}")  # ➕ 어떤 클라이언트가 붙었는지 표시

    while True:
        try:
            data = c.recv(BUFSIZE)

            if not data:  # 클라이언트가 접속을 끊었을 때
                print(f"👋 [연결 종료] 클라이언트 {a}가 나갔습니다.")  # ➕ 종료 로그
                if c in connections:
                    connections.remove(c)
                c.close()
                break

            # 💡 [핵심 추가] 메인 루프에서 지웠던 수신 로그를 여기로 가져왔습니다.
            msg = data.decode("utf-8", errors="ignore")
            print(
                f"📩 [메시지 수신] 클라이언트 {a} ➔ : {msg.strip()}"
            )  # ➕ 누가 보냈는지 주소(a)와 메시지(msg)를 매핑해 출력

            for connection in connections:
                connection.send(data)

        except Exception as e:
            # ➕ 멀티스레드 환경에서 한 명이 갑자기 튕겼을 때 서버 전체가 죽지 않도록 방어 코드 추가
            if c in connections:
                connections.remove(c)
            c.close()
            break

PORT = 2100
BUFSIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("",PORT))
sock.listen(1)
connections = []

print("====> server start") 

msg = ''
while True:
    c, a= sock.accept()
    cThred = threading.Thread(target=handler, args=(c,a))
    cThred.daemon=True
    cThred.start()
    connections.append(c)

    print(f"connection ===> {connections}")

 

