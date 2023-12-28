import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(("localhost", 9000))
cmd = "GET https://localhost/index.html HTTP/1.0\r\n\r\n".encode()
cliente.send(cmd)

while True:
    data = cliente.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end=' ')
cliente.close()
