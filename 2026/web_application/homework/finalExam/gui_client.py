from socket import *
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from threading import *

class ChatClient:
    client_socket = None

    def __init__(self, ip, port):
        self.initalize_socket(ip, port)
        self.initalize_gui()
        self.listen_thread()
    
    def initalize_socket(self, ip, port):
        '''
        TCP socket을 생성하고 server와 연결
        '''
        self.client_socket = socket(AF_INET, SOCK_STREAM)
        remote_ip = ip
        remote_port = port
        self.client_socket.connect((remote_ip, remote_port))
        

    def send_chat(self):
        '''
        emssage를 전송하는 버튼 콜백함수
        '''

        senders_name = self.name_widget.get().strip() +":"
        data = self.enter_text_widget.get(1.0, 'end').strip()
        message = (senders_name + data).encode('utf-8')+'\n'

        self.chat_transcript_area.yviewk