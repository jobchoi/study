import sys
from socket import *
import cal_echo_M

ECHO_PORT = 2500
BUFSIZE = 1024

if len(sys.argv) > 1:
    port = int(eval(sys.argv[1]))
else:
    port = ECHO_PORT

s= socket(AF_INET, SOCK_STREAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR,1)
s.bind(('',port))
s.listen(1)

print("Waitting for connetion from client")
conn, (remotehost, remoteport) = s.accept()
print(f'connected by :{remotehost} / {remoteport} ')




while True:
    try :
        data = conn.recv(BUFSIZE)

        if not data:
            print("데이타가 없음, 연결 종료")
            break
        # data = float(data.decode())        
        # data = 9.0/5.0*data+32.0
        # data = '{:.1f}'.format(data)
        # conn.send(data.encode())
        
        spldata = data.decode().strip()
        result_cal = cal_echo_M.CalEchoM.cal_task(spldata)
        conn.send(result_cal.encode())
    except:
        pass
    else:
        conn.close()

