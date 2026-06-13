from asyncio import sleep, wait
# from tkinter import *
import tkinter as tk
# from socket import *
import socket
import threading
import struct

BUFSIZE = 1024
PORT = 2000

def calculate():
    global temp
    # temp = float(entry1.get())
    sendMsg = str(entry1.get())
    # sock.send(str(temp).encode())
    sock.send(sendMsg.encode()) 
    print(f"====> chk Send data: {sendMsg}")   

def handler(sock):
    while True:
        try :
            r_msg = sock.recv(BUFSIZE)
            print(f"====> chk Received data: {r_msg.decode()}")
        except EOFError as eof:
            print(" ==> EOFError: ", eof)
            break
            # pass
        else:
            entry2.delete(0,tk.END)
            entry2.insert(0,r_msg.decode())
            entry1.delete(0, tk.END)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost",PORT))

root = tk.Tk()
message_label = tk.Label(text='Enter a temperture(C)',font=('Verdana',16))
entry1 = tk.Entry(font=('Verdana',16),width=5)
recv_label = tk.Label(text='Temperature in F', font=('Verdana',16))
entry2 = tk.Entry(font=('Verdana',16),width=5)

calc_button = tk.Button(text='전송', font=('Verdana',12),command=calculate)

message_label.grid(row=0, column=0, sticky=tk.W)
recv_label.grid(row=1,column=0,sticky=tk.W)
entry1.grid(row=0,column=1)
entry2.grid(row=1,column=1)
calc_button.grid(row=0, column=2, padx=10,pady=10)

# 데이터 수신을 위한 스레드 생성과 실행
cThread = threading.Thread(target=handler, args=(sock,))
cThread.daemon = True
cThread.start()

root.mainloop()