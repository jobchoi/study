import socket
import os
import sys

port = 5100
s_sock = socket.socket()
host = ""
s_sock.bind((host, port))
s_sock.listen(1)

print("Waiting for connection...")

c_sock, addr = s_sock.accept()
print(f"Connection from {addr} has been established.")
msg = c_sock.recv(1024)
print(msg.decode())

filename = input("Enter the filename to send(./test/sample.txt): ")
if not os.path.isfile(filename):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(base_dir, filename)
    clean_filename = filename.split("./")
    filename = os.path.join(base_dir, clean_filename[-1])

    if not os.path.isfile(filename):
        print("File does not exist.")
        c_sock.close()
        sys.exit()
print(f"Sending file: {filename}")

fn = filename.split("/")

c_sock.send(fn[-1].encode())

with open(filename, "rb") as f:
    c_sock.sendfile(f, 0)

    # while True:
    #     data = f.read(1024)
    #     if not data:
    #         break
    #     c_sock.send(data)
print("Sending complete.")
c_sock.close()