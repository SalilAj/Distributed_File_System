import socket
import threading


def main():
    try:
        server = TCPServer()
        server.listen()
    except socket.error, errorMsg:
        print "Failed to create a socket" + str(errorMsg)

class TCPServer(object):

	port = 8000
	host = "127.0.0.0"

	def listen(self):
		self.socketConn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socketConn.bind((self.host,port))
		self.sock.listen()
		self.sock.accept()
		print("connected")




		


if __name__ == "__main__": main()