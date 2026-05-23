# 송수신 예외처리를 한 에코 서버

import cal_echo_M
import setupSocket_M

PORT = 2000
BUFSIZE = 1024

sock = setupSocket_M.setUp_server(PORT, BUFSIZE)

c_sock, (r_host,r_port) = sock.accept()
# print(f"Connected by {r_host}, {r_port}")

while True:
    try:
        # data=sock.recv(BUFSIZE)
        data=c_sock.recv(BUFSIZE)
        
        if not data:
            c_sock.close()
            print("연결이 종료되었습니다 - 1")
            break
        spldata = data.decode().strip()
        result_cal = cal_echo_M.CalEchoM.cal_task(spldata)
        c_sock.send(str(result_cal).encode())
    except:
        print("연결이 종료되었습니다 - 2")
        print(f"============> Send : {c_sock} - chk#1" )
        c_sock.close()
        break
    else:
        print(data.decode())
        spldata = data.decode()

        calM = cal_echo_M.CalEchoM()

        # is_valid = cal_echo_M.chk_input(spldata)
        is_valid = calM.chk_input(calM) 

        print(f"chk_input : {is_valid}")   
        

        if not is_valid:
            sock.send("연산자 오류".encode())
            continue


#       C -> S 입력된 문자열에서 연산자를 체크
        if not is_valid:
            sock.send("연산자 오류".encode())
            continue    

        result_cal = calM.cal_task(calM )

        try:
            print(f"============> Send : {result_cal} - chk#2" )
            sock.send(str(result_cal).encode())
        except:
            print("연결이 종료되었습니다 - 3")
            sock.close()
            break   

