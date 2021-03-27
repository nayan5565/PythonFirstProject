import socket

s = socket.socket()
print('Socket create')
s.bind(('localhost', 9999))
s.listen(3)
print('Waiting for connection')

while True:
    c, addr = s.accept()
    name = c.recv(1024).decode()
    print("connected with ", addr, name)

    c.send(bytes('Welcome to nayans server', 'utf-8'))

    c.close()
