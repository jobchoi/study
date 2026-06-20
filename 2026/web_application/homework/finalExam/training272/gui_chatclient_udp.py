from socket import *
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from threading import *
import sys

class ChatClient:
    client_socket = None

    def __init__(self, ip, port):
        # UDP 연동을 위한 인자값 클래스 내 보존
        self.server_ip = ip
        self.server_port = port
        
        self.initialize_socket(ip, port)
        self.initialize_gui()
        self.listen_thread()

    def initialize_socket(self, ip, port):
        '''
        [수정 완료] UDP(SOCK_DGRAM) 소켓 생성 (connect는 제거)
        '''
        # SOCK_STREAM에서 SOCK_DGRAM으로 전면 교체
        self.client_socket = socket(AF_INET, SOCK_DGRAM)
        print(f"UDP 클라이언트 소켓이 준비되었습니다. 대상 서버 -> {ip}:{port}")

    def send_chat(self):
        '''
        [수정 완료] message를 sendto() 방식으로 전송하는 버튼 콜백 함수
        '''
        senders_name = self.name_widget.get().strip() + ":"
        data = self.enter_text_widget.get(1.0, 'end').strip()
        
        if not data: # 빈 메시지 연타 차단
            return 'break'
            
        message = (senders_name + data).encode('utf-8')
        
        # 내 화면(ScrolledText)에 전송한 메시지 출력
        self.chat_transcript_area.insert('end', senders_name + data + '\n')
        self.chat_transcript_area.yview('end')
        
        try:
            # [핵심 수정] UDP이므로 send 대신 sendto를 쓰고 목적지 주소 튜플을 전달합니다.
            self.client_socket.sendto(message, (self.server_ip, self.server_port))
        except Exception as e:
            print(f"데이터그램 전송 실패: {e}")
            
        self.enter_text_widget.delete(1.0, 'end')
        return 'break'
    
    def initialize_gui(self):
        '''
        위젯을 배치하고 초기화 (TCP 예제와 100% 동일한 화면 구성)
        '''
        self.root = Tk()
        self.root.title("UDP GUI 멀티 채팅 클라이언트")
        
        fr = []
        for i in range(0, 5):
            fr.append(Frame(self.root))
            fr[i].pack(fill=BOTH)
        
        self.name_label = Label(fr[0], text='user name')
        self.recv_label = Label(fr[1], text='read msg')
        self.send_label = Label(fr[3], text='write msg')
        self.send_btn = Button(fr[3], text='push', command=self.send_chat)
        self.chat_transcript_area = ScrolledText(fr[2], height=20, width=60)

        self.enter_text_widget = ScrolledText(fr[4], height=5, width=60)
        self.name_widget = Entry(fr[0], width=15)

        self.name_label.pack(side=LEFT)
        self.name_widget.pack(side=LEFT)
        self.recv_label.pack(side=LEFT)
        self.send_btn.pack(side=RIGHT, padx=20)
        self.chat_transcript_area.pack(side=LEFT, padx=2, pady=2)
        self.send_label.pack(side=LEFT)
        self.enter_text_widget.pack(side=LEFT, padx=2, pady=2)

    def listen_thread(self):
        '''
        데이터 수신 Thread 를 생성하고 시작한다.
        '''
        t = Thread(target=self.receive_message, args=(self.client_socket,))
        t.daemon = True # 창 닫으면 수신 스레드도 함께 정상 소멸하도록 데몬 설정
        t.start()

    def receive_message(self, so):
        '''
        [수정 완료] recvfrom() 을 이용한 비연결형 데이터 수신
        '''
        while True:
            try:
                # [핵심 수정] UDP이므로 recv 대신 recvfrom을 사용합니다.
                # buf: 데이터, addr: 보낸 사람의 주소 튜플
                buf, addr = so.recvfrom(2565)
                
                decoded_msg = buf.decode('utf-8')
                
                # 스레드 충돌(Race Condition)을 원천 방지하기 위해 after_idle로 메인스레드에 양보
                self.root.after_idle(lambda m=decoded_msg: self.update_ui(m))
                
            except Exception as e:
                print(f"UDP 데이터그램 수신 오류 또는 소켓 종료: {e}")
                break
        so.close()

    def update_ui(self, msg):
        ''' 안전한 메인 스레드 UI 업데이트 헬퍼 함수 '''
        self.chat_transcript_area.insert('end', msg + '\n')
        self.chat_transcript_area.yview(END)

if __name__ == "__main__":
    ip = input("server IP addr : ")
    if ip == "":
        ip = "127.0.0.1"
    port = 2500
    ChatClient(ip, port)                                
    mainloop()