import socket
import threading
import Queue
import os

from mainServer import TCPServer

def main():
    try:
        TFS = TFS(8001)
        TFS.listen()
    except socket.error, errorMsg:
        print "Failed to create a socket" + str(errorMsg)

class TFS(TCPServer):

	fileDirectoryLocation = os.getcwd()
    fileDirectoryName = "Files"
    fileDirectoryPath = os.path.join(fileDirectoryLocation, fileDirectoryName)

    def __init__(self, port_use=None):
        TCPServer.__init__(self, port_use, self.func)

    def func():
    	if message == 'UPLOAD':
            self.uploadFile(conn, address, message)
        elif message == 'DOWNLOAD':
            self.downloadFile(conn, address, message)
        else:
            return False

    def uploadFile(self, connection, address, message):
        filename, data = self.execute_write(message)
        con.sendall("File Uploaded")
        return

    def downloadFile(self, connection, address, message):
        filename = message
        path = os.path.join(self.fileDirectoryPath, filename)
        fileCursor = open(path, "w+")
        userFile = fileCursor.read()
        return_string = 'DOWNLOAD FILE:' % (base64.b64encode(userFile))
        con.sendall(return_string)
        return


if __name__ == "__main__": main()