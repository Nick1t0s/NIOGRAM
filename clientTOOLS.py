import socket,pickle
class User:
    def __init__(self,name,hash):
        self.name=name
        self.hash=hash
    def connectAndSend(self,to):
        text=input()
        sock = socket.socket()
        sock.connect(('localhost', 9090))
        sock.send(pickle.dumps({"type":"send","fromHash":self.hash,"toHash":to,"text":text}))
        res=sock.recv(1024).decode()
        if res=="done":
            print("done")
        elif res=="noUser":
            print("noUser")
        sock.close()
    def getData(self):
        sock = socket.socket()
        sock.connect(('localhost', 9090))
        sock.send(pickle.dumps({"type":"get","fromHash":self.hash}))
        data=pickle.loads(sock.recv(1024))
        sock.close()
        print(*data)
x=User("123","3")
x.getData()