import socket
import pickle
sock = socket.socket()
sock.connect(('localhost', 9090))
x=pickle.dumps([1,2,3])
sock.send(x)

sock.close()