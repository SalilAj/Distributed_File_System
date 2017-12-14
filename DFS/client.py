import socket
import threading
import Queue
import os


class DFSclient(object):

	rootLocation = os.getcwd()
	fileFolder = "clientUpload"
	fileLocation = os.path.join(rootLocation, fileFolder)

	host = 'localhost'
	def __init__(self, port=None, handler=None):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.bind((self.host,port))

		self.handler = handler
		self.threadQueue = Queue.Queue(maxsize=15)

		for i in xrange(15):
			thread = ThreadHandler(self.threadQueue, 4096, self)
			thread.setDaemon(True)
			thread.start()

    def open(self, filename):
        file_downloaded = False
        if filename not in self.open_files.keys():
            # Get the info of the server hosting the file
            request = self.__get_directory(filename)
            if re.match(self.SERVER_RESPONSE, request):
                params = request.splitlines()
                server = params[0].split()[1]
                port = int(params[1].split()[1])
                open_file = params[2].split()[1]
                # Get lock on file before downloading
                self.__lock_file(filename, 10)
                file_downloaded = self.__download_file(server, port, open_file)
                if file_downloaded:
                    self.open_files[filename] = open_file
        return file_downloaded

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
	connection = DFSclient(8000)
	print "Enter value"
	inputValue = raw_input()
	if inputValue == 'exit':
		connection.close()
	elif inputValue == 'upload':
		connection.open(inputValue)
		connection.write(inputValue, fileData)
		connection.close(inputValue)

if __name__ == "__main__": main()