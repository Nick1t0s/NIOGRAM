import socket
import pickle
x=pickle.dumps([1,2,3])
sock = socket.socket()
sock.bind(('0.0.0.0', 9090))
sock.listen(1)
conn,addr=sock.accept()
xx=conn.recv(1024)
xx=pickle.loads(xx)
print(xx)