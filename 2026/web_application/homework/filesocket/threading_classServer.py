import socket,threading



class ClientThread(threading.Thread):
    def __init__(self,clientAddress,clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print("New Socket added : ", clientAddress)

    def run(self):
        print("Connection from : ",clientAddress, clientAddress)

    
