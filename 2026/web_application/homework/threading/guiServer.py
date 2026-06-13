import sys
# from socket import *
import socket   
import cal_echo_M

ECHO_PORT = 2000
BUFSIZE = 1024

if len(sys.argv) > 1:
    port = int(eval(sys.argv[1]))
else:
    port = ECHO_PORT

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
s.bind(('',port))
s.listen(1)

print("Waitting for connetion from client")
conn, (remotehost, remoteport) = s.accept()
print(f'Connected by :{remotehost} / {remoteport} ')


calM = cal_echo_M.CalEchoM()  
result_cal = ''


while True:
    
    try :
        print("Waiting for data from client...")
        data = conn.recv(BUFSIZE)

        print(f"====> chk Received data: {data.decode()}")
        if not data:
            print("데이타가 없음, 연결 종료")
            break
        # data = float(data.decode())        
        # data = 9.0/5.0*data+32.0
        # data = '{:.1f}'.format(data)
        # conn.send(data.encode())
        
        spldata = data.decode().strip()

        print(f"==> Received data: {spldata}")

        result_cal = calM.cal_task(spldata)
        conn.send(str(result_cal).encode())
    except ValueError as ve:
        print(f"Value error: {ve}")
        conn.send("입력 오류 - 숫자만 입력해주세요.".encode())
        continue
    except Exception as e:
        print(f"Error occurred: {e}")
        conn.send("서버 오류 - 다시 시도해주세요.".encode())
        break
    else:
        conn.close()
