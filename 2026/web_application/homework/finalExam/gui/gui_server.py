import sys
from socket import *

ECHO_PORT = 2500
BUFSIZE = 1024

if len(sys.argv) > 1:
    port = int(sys.argv[1])
else:
    port = ECHO_PORT

s = socket(AF_INET, SOCK_STREAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('', port))
s.listen(1)

print(f"Calculator Server waiting on Port {port}...")
conn, (remotehost, remoteport) = s.accept()
print(f"Connected by {remotehost}:{remoteport}")

while True:
    try:
        # 클라이언트의 수식 패킷 대기 (예: "2+3")
        data = conn.recv(BUFSIZE)
        
        # 상대방이 close하면,  무한루프 방지 탈출
        if not data:
            print("데이터가 없거나 클라이언트가 연결을 종료했습니다.")
            break
            
        # 데이터 해독 및 공백 제거
        expr = data.decode().strip()
        print(f"Received expression: {expr}")
        
        # 수식을 안전하게 계산 (파이썬 내장 eval 활용)
        try:
            # 안전하게 수식을 연산하고 문자열로 고정
            result = str(eval(expr))
            print(f"결과 : {result}")
        except ZeroDivisionError:
            result = "Error: 0으로 나눌 수 없습니다."
        except Exception:
            result = "Error: 잘못된 수식입니다."
            
        # 결과 송신 (무조건 문자열 강제 랩핑 후 encode)
        conn.sendall(result.encode())
        
    except Exception as e:
        # 소켓 세션 자체가 깨진 경우
        print(f"치명적인 통신 예외 발생: {e}")
        break

# while 루프가 완전히 끝난 바깥에서 소켓을 딱 한 번 정상 수거
conn.close()
s.close()
print("서버가 종료되었습니다.")