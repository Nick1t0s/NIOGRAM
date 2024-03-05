import socket,pickle
class User:
    def __init__(self,name,hash):
        self.name=name
        self.hash=hash
    def connectAndSend(self,to):
        text=input("Get: ")
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
    def register(self):
        while True:
            sock = socket.socket()
            sock.connect(('localhost', 9090))
            hashReg=input("Please give me hash: ")
            if not hashReg[0]=="@":
                sock.close()
                continue
            sock.send(pickle.dumps({"type":"checkHash","hash":"hash"}))
            res=sock.recv(1024).decode()
            if res=="1":
                print("Please enter another hash because this one is busy")
                sock.close()
                continue
            else:
                print(res)
                print('done')
                isPass=True
                while isPass:
                    passWord=input("Plesae give me a password: ")
                    if len(passWord)>6:
                        isPass=False
                    else:
                        print("Your password must be at least 6 characters long")
                sock.close()
                sock = socket.socket()
                sock.connect(('localhost', 9090))
                sock.send(pickle.dumps({"type":"RegUser","hash":hashReg,"pass":passWord}))
                res=sock.recv(1024).decode()
                if res=="done":
                    print("You have successfully registered")
                elif res=="hashErr":
                    print("While you were trying to come up with a passcode, someone else had already used this hash.")
                    continue
                elif res=="someErr":
                    print("Something weird happened. Try again later, maybe?")
                break

    def GetCheckAnd(self):
        hashTag=input("Please enter your hash: @")
        passWord=input("Please enter your password: ")
        while self.checkUncalHash(hashTag):
            print('Please enter another hash because this one is busy')
            hashTag=input("Please ")
    def checkUncalHash(self,hashTag):
        sock=socket.socket()
        sock.send(pickle.dumps({"type": "checkHash", "hash": hashTag}))
        res=sock.recv(1024) #1 Плохо 0 хорошо
        return res
    def checkPassword(self,passWord)
        return 1

x=User("123","@2")
while True:
    tx=input()
    if tx=="get":
        x.getData()
    elif tx=="send":
        x.connectAndSend("@3")
    elif tx=="reg":
        x.register()