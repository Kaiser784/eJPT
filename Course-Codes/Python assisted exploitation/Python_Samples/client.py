# eLearnSecurity 2013

import socket

SER_ADDR = input("Type the server IP address: ")
SER_PORT = int(input("Type the server port: "))

my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_sock.connect((SER_ADDR, SER_PORT))
print("Connection established")

message = input("Message to send: ")
my_sock.sendall(message)
my_sock.close()
