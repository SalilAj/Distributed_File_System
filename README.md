# Distributed_File_System
Distributed File System - Scalable computing

This is a Distributed File system coded in python.

Scalable Computing Assignment 3:

Name: Salil Ajgaonkar TCD ID: 17317640

How to Run?

Clone the repository
(make sure all the python dependencies are installed)
run the directoryServiceSys.py server using the below command
Command: $ python directoryServiceSys.py
run the transparentFileSystem.py server using the below command
Command: $ python transparentFileSystem.py
run the client.py server using the below command
Command: $ python client.py

Description: This project was developed with the intention of setting up independent servers communicationg via socket messages to provide a cloud file system in a distributed manner.

It provides a basic functionality of file system where you can upload and download files and edit or delete them.
This system was developed with the intention of providing the following services:

1) File System Server:
A flat file directory service where you can upload and download files from remote storage.
Currently able to upload and download files.

2) File Directory system:
This server keeps a track of all the file servers currently runnin in the System and which server holds which file.
The track of the server's is maintained by this server using MongoDB as its Database.

3) Locking Server:
Next in developement was the locking server. File editing services would be provided by the File server during which the locking server would lock the file currently being edited by the User.

4) Replication:
After the developement of the Locking server the next service planned to be developed was the Replication server. Multiple File servers may contain different files. If any one server crashed, access to the files on those servers would be restricted. Replication provides a solution to this issue. Replication replicates the files among a set of servers which together form a cluster. if any one server in a cluster goes down the other servers still make the files accessible.

Current Issue: Needed more time to develop the entire system. Was only able to implement the File server and Directory server and was under the process of creating a client before deadlines approached. once Client was set up I would have been able to implement editing functionality in the File Server which is an important criteria for developing the next service that is the Locking system. Implementation of the Locking system would led to the development of a proper DFS with CRUD operations. once this system is setup the last leg of development would have been the Replication server which would constantly run in the bakgrounf replicating the files among servers in a cluster.

Due to the vastness of this project I referred to the DFS system already developed by a developer named PinPinIre (git repo attached). However it was only used as a reference to keep the bigger picture in mind. The code has been coded by me in Python and MongoDB

REFERENCE:
https://github.com/PinPinIre/CS4032-Distributed-File-System
