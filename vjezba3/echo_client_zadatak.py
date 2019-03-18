import socket
import datetime
from local_machine.info import print_machine_info

print datetime.datetime.now()

print("Hostname: ", hostname)
print("IP Address: ", addr)

host = socket.gethostname()
port = 9999
client_socket = socket.socket()

client_socket.connect((host,port))

text = raw_input('Unesite tekst: ')
print text

data = client_socket.recv(1024)

print data
client_socket.close()