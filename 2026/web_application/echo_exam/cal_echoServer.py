# 송수신 예외처리를 한 에코 서버

from socket import *

PORT = 2100
BUFSIZE = 1024

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('',PORT))
sock.listen(5)
print("Waiting for clients")

c_sock, (r_host,r_port) = sock.accept()
print(f"Connected by {r_host}, {r_port}")

while True:
    try:
        data=c_sock.recv(BUFSIZE)
        
        if not data:
            c_sock.close()
            print("연결이 종료되었습니다")
            break
    except:
        print("연결이 종료되었습니다.")
        c_sock.close()
        break
    else:
        print(data.decode())
        spldata = data.decode()

        if "+" in spldata:
            print("+ chk : OK")
            getData = int(spldata.split("+"))
            print(f"{getData[0] + getData[1]}")

        elif "-" in spldata:
            print("-")
        elif "*" in spldata:
            print("*")
        elif "/" in spldata:
            print("/")

        else:
            print("입력 오류")
        
        
            # print(f"{spldata.split()}")
            # print(f"result : {spldata.split('+')}")


    try:
        c_sock.send(data)
    except:
        print("연결이 종료되었습니다.")
        c_sock.close()
        break
        

