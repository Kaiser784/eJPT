# eLearnSecurity 2013

import http.client

host = input("Insert the host/IP: ")
port = input("Insert the port(default:80): ")
url = input("Insert the url: ")

if(port == ""):
    port = 80

try:
    connection = http.client.HTTPConnection(host, port)
    connection.request('GET', url)
    response = connection.getresponse()
    print("Server response:",response.status)
    connection.close()
except ConnectionRefusedError:
    print("Connection failed")


