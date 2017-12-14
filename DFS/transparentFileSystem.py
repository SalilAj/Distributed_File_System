import socket
import threading
import Queue
import os
import base64

from mainServer import TCPServer

class TFS(TCPServer):
    fileDirectoryLocation = os.getcwd()
    fileDirectoryName = 'Files'
    fileDirectoryPath = os.path.join(fileDirectoryLocation, fileDirectoryName)

    def __init__(self, port_use=None):
        TCPServer.__init__(self, port_use, self.func)

    def func(self, connection, address, message):
        print(message)
    	if message == 'UPLOAD':
            self.huploadFile(connection, address, message)
        elif message == 'DOWNLOAD':
            self.hdownloadFile(connection, address, message)
        else:
            return False

    def huploadFile(self, connection, address, message):
        request = message.splitlines()
        filename = request[0].split()[1]
        data = request[1].split()[1]
        data = base64.b64decode(data)

        path = os.path.join(self.fileDirectoryPath, filename)
        fileWriter = open(path, "w+")
        fileWriter.write(data)

        return_string = "File Uploaded"
        connection.sendall(return_string)
        return

    def hdownloadFile(self, connection, address, message):
        request = message.splitlines()
        filename = request[0].split()[1]
        path = os.path.join(self.fileDirectoryPath, filename)
        fileReader = open(path, "w+")
        dataFile = fileReader.read()

        return_string = "File Downloaded: %s\n" + (base64.b64encode(dataFile))
        connection.sendall(return_string)
        return

def main():
    try:
        server = TFS(8001)
        server.listen()
    except socket.error, errorMsg:
        print "Failed to create a socket" + str(errorMsg)

if __name__ == "__main__": main()