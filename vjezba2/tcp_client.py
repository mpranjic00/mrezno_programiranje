import socket

client_socket = socket.socket()
host = socket.gethostbyname('www.google.hr')
port = 80

print host
client_socket.connect((host, port))
# print client_socket.recv(1024)
client_socket.close()