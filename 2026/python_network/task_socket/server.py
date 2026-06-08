# import socket
# import time

# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# address = ('',5500)

# sock.bind(address)
# sock.listen(5)
# cnt = 0

# while True:
#     client, addr = sock.accept()
#     print(f"당신은 {cnt}번째 접속자 입니다. ",addr)
#     client.send(time.ctime(time.time()).encode())
#     client.close()
#     cnt +=1


import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


address = ('',5500)

cnt = 0

sock.bind(address)


sock.listen(5)



while True:
    client, addr1 = sock.accept()
    

    if addr1 == 5501 :
        print(f"port 확인 : {cnt} . ",addr1)
        client.send(time.ctime(time.time()).encode())    

#     client.close()