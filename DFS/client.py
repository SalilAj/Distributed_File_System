import socket
import threading
import Queue
import os


class DFSclient(object):

	server = 'localhost'
	rootLocation = os.getcwd()
	fileFolder = "clientUpload"
	fileLocation = os.path.join(rootLocation, fileFolder)

	host = 'localhost'

	def __init__(self, port=None):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.threadQueue = Queue.Queue(maxsize=1)

	def open(self, filename):
		request = self.getDirectory(filename)
		connection.sendall(return_string)

	def getDirectory(self, filename):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.connect((self.server, 8002))
		sock.sendall(filename)
		while True:
			data = sock.recv(4026)
			returnData = data
			print returnData
			sock.close()
			sock = None
			return returnData


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
			print(data)
			if len(data) != 0 and len(data) < self.bufferLength:
				if len(data) > 0:
					if data == 'hi':
						self.server.hello(connection, address, data)
					else:
						self.messageHandler(connection, address, data)
		return

def main():
	path = os.path.join(DFSclient.fileLocation, "salil")
	fileData = open(path, "rb").read()
	connection = DFSclient(8010)
	print "Enter value"
	inputValue = raw_input()
	msg = inputValue.split(':')
	if msg[0] == 'exit':
		connection.close()
	elif msg[0] == 'upload':
		connection.open(msg[1])
		connection.write(inputValue, fileData)
		connection.close(inputValue)
	elif msg[0] == 'download':
		return False

if __name__ == "__main__": main()