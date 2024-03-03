import socket

sock = socket.socket()
sock.connect(('localhost', 9090))
sock.send('hello, world!'.encode())

sock.close()
