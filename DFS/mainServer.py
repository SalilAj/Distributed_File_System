import socket
import threading
import Queue


class TCPServer(object):

	host = 'localhost'
	def __init__(self, port=None, handler=None):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.bind((self.host,port))

		self.handler = self.testHandler
		self.threadQueue = Queue.Queue(maxsize=15)

		for i in xrange(15):
			thread = ThreadHandler(self.threadQueue, 4096, self)
			thread.setDaemon(True)
			thread.start()

	def testHandler(self):
		return True

	def listen(self):
		self.sock.listen(5)
		while True:
			connection, address = self.sock.accept()
			self.threadQueue.put((connection, address))
			print("connected")

class ThreadHandler(threading.Thread):

	def __init__(self, threadQueue, bufferLength, server):
		threading.Thread.__init__(self)
		self.server=server
		self.queue = threadQueue
		self.bufferLength = bufferLength
		self.messageHandler = server.handler

	def run(self):
		while True:
			request = self.queue.get()
			self.handler(request)
			self.queue.task_done()

	def handler(self, (connection, address)):
		while True:
			data = connection.recv(self.bufferLength)
			if len(data) != 0 and len(data) < self.bufferLength:
				if len(data) > 0:
					print data
		return


def main():
    try:
        server = TCPServer(8001)
        server.listen()
    except socket.error, errorMsg:
        print "Failed to create a socket" + str(errorMsg)



if __name__ == "__main__": main()