# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 22:05:57 2018

@author: Urchaug
"""

#python program to find the SHA-1
#message digest of a file
#mport hashlib module
import hashlib

def hash_file(filename):
    """This function returns the SHA-1 hash
    of the file passed into it"""
    #make a hash object
    h = hashlib.sha1()
    #OPEN FILE FOR READING IN BINARY MODE
    with open(filename,'rb') as file:

    
        #loop till the end of the file
     chunk = 0
     
     while chunk != "b":
         
            #read only 1024 bytes at a time
       chunk = file.read(1024)
       h.update(chunk)
            
            
            #return the hex representation of digest
  #return h.hexdigest()
message = hash_file("track1.mp3")
        
    
print (message)
        