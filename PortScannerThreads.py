from socket import *
import threading
from time import sleep

serverName = "localhost"
open_ports = []
testedPorts = 0


def test_port(port):
    try:
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((serverName, port))
        clientSocket.close()
        open_ports.append(port)
        print("Able to establish a connection to port: " + str(port))
        global testedPorts
        testedPorts = testedPorts + 1
    except:
        print("Not able to establish a connection to port: " + str(port))
        testedPorts = testedPorts + 1


for serverPort in range(1000):
    threading.Thread(target=test_port, args=(serverPort,)).start()

# waiting for all threads to finish
while testedPorts < 1000:
    sleep(0.5)
    print("sleeping:" + str(testedPorts))
print("Open ports:" + str(open_ports))
