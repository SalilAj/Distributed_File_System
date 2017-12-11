import socket
import threading
import Queue

from mainServer import TCPServer

def main():
    try:
        TFS = TFS(8001)
        TFS.listen()
    except socket.error, errorMsg:
        print "Failed to create a socket" + str(errorMsg)

class TFS(TCPServer):

    def __init__(self, port_use=None):
        TCPServer.__init__(self, port_use, self.func)

    def func():
    	return False;



if __name__ == "__main__": main()