import sys
import time
from tkinter import *
from socket import *
import threading

BUFSIZE = 1024
PORT = 2500

# 전송 버튼 클릭 시 동작 함수
def calculate():
    sendMsg = str(entry1.get()).strip()
    if not sendMsg: # 빈 문자열이면 전송하지 않고 함수 종료
        return
        
    try:
        sock.send(sendMsg.encode())
        print(f"====> Sent to Server: {sendMsg}")
    except Exception as e:
        print(f"데이터 전송 실패: {e}")

# 백그라운드 수신 전용 스레드 핸들러
def handler(sock):
    while True:
        try:
            r_msg = sock.recv(BUFSIZE)
            
            # 서버가 close했을 때 들어오는 b'' 패킷 검출 -> 수신 스레드 소멸
            if not r_msg:
                print("서버가 연결을 종료했습니다. Thread End")
                break
                
            decoded_msg = r_msg.decode().strip()
            print(f"====> Received from Server: {decoded_msg}")
            
            # else 에러가 나는 부분을 try 내부에서 순차적으로 GUI 컴포넌트 즉시 갱신하도록 변경
            entry2.delete(0, END)
            entry2.insert(0, decoded_msg)
            entry1.delete(0, END)
            
        except Exception as e:
            print(f"데이터 수신 모듈 예외 발생: {e}")
            break

# 소켓 연결 설정 단계
sock = socket(AF_INET, SOCK_STREAM)
try:
    sock.connect(('localhost', PORT))
except ConnectionRefusedError:
    print("서버가 구동되어 있지 않습니다! 서버(eval_server.py)를 먼저 실행하세요.")
    sys.exit()

# Tkinter 윈도우 메인 프레임 설정
root = Tk()
root.title("GUI 사칙연산 계산기")


message_label = Label(root, text="사칙연산을 입력해주세요 (Ex:5*3):", font=("Verdana", 14))
entry1 = Entry(font=("Verdana", 14), width=12)

recv_label = Label(text='Calculation Result:', font=("Verdana", 14))
entry2 = Entry(font=("Verdana", 14), width=12)

calc_button = Button(text="Send", font=("Verdana", 12, "bold"), bg="#10b981", fg="black", command=calculate)

# 컴포넌트 배치를 그리드 방식으로
message_label.grid(row=0, column=0, sticky=W, padx=10, pady=5)
recv_label.grid(row=1, column=0, sticky=W, padx=10, pady=5)
entry1.grid(row=0, column=1, padx=10, pady=5)
entry2.grid(row=1, column=1, padx=10, pady=5)
calc_button.grid(row=0, column=2, rowspan=2, padx=15, pady=10, ipady=10)

# 멀티스레드 기반 수신 감시망 동작 시작 (Daemon 설정으로 GUI 창 꺼지면 스레드도 동시 소멸)
cThread = threading.Thread(target=handler, args=(sock,))
cThread.daemon = True
cThread.start()

mainloop()