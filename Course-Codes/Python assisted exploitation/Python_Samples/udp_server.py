# eLearnSecurity 2013

from socket import *
import sys
import select
address = ('192.168.1.131', 5)
server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(address)

while(1):
    print("Listening")
    recv_data, addr = server_socket.recvfrom(2048)
    print(recv_data)
    if recv_data == "Request 1" :
        print("Received request 1")
        server_socket.sendto("Response 1", "192.168.1.1")
    elif recv_data == "Request 2" :
        print("Received request 2")
        data = b"Response 2"
        server_socket.sendto(data, addr)
    else:
        print("Other")
        data = b"Other"
        server_socket.sendto(data, addr)
