# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 08:26:24 2018

@author: Urchaug
"""

#!/usr/bin/python # this is server.py file
import socket # import socket module
s = socket.socket() # create a socket object
host = socket.gethostname() # get a local machine name
port = 102  # reserve a port for your service
s.bind((host,port)) # bind to the port
s.listen(5) # now wait for client connection
while True:
    c,addr = s.accept() # establish connection with client
print ('got connection from'),addr
c.send ('thanks for connecting')
c.close()  #Close the connection
