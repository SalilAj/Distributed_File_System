import socket
import threading

def main():
    try:
        server = TCPServer(8000)
        server.listen()
    except socket.error, errorMsg:
        print "Failed to create a socket" + str(errorMsg)

if __name__ == "__main__": main()