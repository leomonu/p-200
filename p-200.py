from ipaddress import ip_address
import socket
from threading import Thread

nickName = input("Enter Your Name")


client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ip_address = "127.0.0.1"
port = 8000

client.connect((ip_address,port))

print("Connected with the server")


def received():
    while True:
        try:
            message=client.recv(2048).decode('utf-8')
            if message == "nickName":
                client.send(nickName.encode('utf-8'))
            else:
                print(message)
        except:
            print("an error has occured")
            client.close()
            break

def write():
    while True:
        message="{}:{}".format(nickName,input(" "))
        client.send(message.encode('utf-8'))


receiveThread=Thread(target=received)
receiveThread.start()

writeThread = Thread(target=write)
writeThread.start()