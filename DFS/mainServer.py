import socket
import threading


def main():
    try:
        server = TCPServer(8000)
        server.listen()
    except socket.error, errorMsg:
        print "Failed to create a socket" + str(errorMsg)

class TCPServer(strPort):
	port=strPort
	host = "127.0.0.0"
	def _init_(self):
		self.socketConn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.bind((self.host,port))

		


if __name__ == "__main__": main()