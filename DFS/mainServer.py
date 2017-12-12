import socket
import threading
import Queue

class TCPServer(object):

	host = "127.0.0.0"

	def __init__(self, port=None, handler=None):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.bind((host,port))
		self.handler = handler
		self.threadQueue = Queue.Queue(maxsize=15)

        for i in range(15):
            thread = ThreadHandler(self.threadQueue, 4096, self)
            thread.setDaemon(True)
            thread.start()

	def testHandler(self):
		return True

	def listen(self):
		self.sock.listen()
		self.sock.accept()
		print("connected")	

class ThreadHandler(threading.Thread):
	def __init__(self,threadQueue,bufferLength,server):
		threading.Thread.__init__(self)
		self.server=server
		self.messageHandler=server.handler

	def run(self):
		while True:
			request = self.queue.get()
			self.handler(request)
			self.queue.task_done()


def main():
    try:
        server = TCPServer()
        server.listen()
    except socket.error, errorMsg:
        print "Failed to create a socket" + str(errorMsg)

if __name__ == "__main__": main()