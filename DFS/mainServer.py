import socket
import threading

class TCPServer(object):

	port = 8000
	host = "127.0.0.0"

	def _init_(self):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.bind((self.host,self.port))
		#self.handler = self.testHandler
		thread = ThreadHandler(self)
		thread.setDaemon(True)
		thread.start()

	def testHandler(self):
		return True

	def listen(self):
		self.sock.listen(10)
		self.sock.accept()
		print("connected")	

class ThreadHandler(threading.Thread):
    def __init__(self, thread_queue, buffer_length, server):
        threading.Thread.__init__(self)
        self.queue = thread_queue
        self.buffer_length = buffer_length
        self.server = server
        self.messageHandler = server.handler

    def run(self):
        # Thread loops and waits for connections to be added to the queue
        while True:
            request = self.queue.get()
            self.handler(request)
            self.queue.task_done()

    def handler(self, (con, addr)):
        message = ""
        # Loop and receive data
        while "\n\n" not in message:
            data = con.recv(self.buffer_length)
            message += data
            if len(data) < self.buffer_length:
                break
        # If valid http request with message body
        if len(message) > 0:
            if message == "KILL_SERVICE\n":
                print "Killing service"
                self.server.kill_serv(con)
            elif re.match(self.server.HELO_REGEX, message):
                self.server.helo(con, addr, message)
            elif self.messageHandler(message, con, addr):
                None
            else:
                print message
                self.server.default(con, addr, message)
        return

#class connThread(threading.Thread):
#	def _init_(self, server):
#		threading.Thread._init_(self)
#		self.server = server
#		self.messageHandler = server.testHandler

#	def run(self):
#		while True:
#			request = self.queue.get()
        #self.handler(request)
        #self.queue.task_done()

def main():
    try:
        server = TCPServer()
        server.listen()
    except socket.error, errorMsg:
        print "Failed to create a socket" + str(errorMsg)

if __name__ == "__main__": main()