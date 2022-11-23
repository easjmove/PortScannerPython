from socket import *

serverName = "localhost"
open_ports = []
for serverPort in range(1000):
    try:
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((serverName, serverPort))
        clientSocket.close()
        open_ports.append(serverPort)
        print("Able to establish a connection to port: " + str(serverPort))
    except:
        print("Not able to establish a connection to port: " + str(serverPort))
print(open_ports)
