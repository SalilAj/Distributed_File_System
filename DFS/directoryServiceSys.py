import socket
import threading
import Queue
import os
import base64
from pymongo import MongoClient
from pprint import pprint

from mainServer import TCPServer

class DSSystem(TCPServer):

    client = MongoClient('mongodb://localhost:27017/')
    db = client['DFS']
    collectionServer= db['server']
    collectionDirectories = db['directories']

    def __init__(self, port_use=None):
        TCPServer.__init__(self, port_use, self.handler)

    def handler(self, connection, address, message):
        print(message)
    	returnString = self.getServers(connection, address, message)
        print returnString

    def getServers(self, connection, address, message):
        request = message.splitlines()
        host, port = self.findServer(request[0])
        returnString = 'HOST:%s,PORT:%s' % (host, port)
        return returnString

    def findServer(self, filename):
        serverDetails = (False, False)
        print filename
        doc = self.collectionDirectories.find_one({"path":str(filename)})
        print doc['server']
        serverDoc = self.collectionServer.find_one({"server":doc['server']})
        print serverDoc['host']
        return serverDoc['host'], serverDoc['port']

    
def main():
    try:
        server = DSSystem(8002)
        server.listen()
    except socket.error, errorMsg:
        print "Failed to create a socket" + str(errorMsg)

if __name__ == "__main__": main()