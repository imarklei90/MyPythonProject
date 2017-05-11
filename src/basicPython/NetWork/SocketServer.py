import socket

s = socket.socket()

host = socket.gethostname()
port = 1234
s.bind((host, port))

s.listen(5)

while True:
    c.addr = s.accept()
    print "get Connection from :", addr
    c.send('3q Connect Success')
    c.close()