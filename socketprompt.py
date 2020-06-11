#This example just explains how to take input for url from user 
#And creating request response cycle by GET request keyword

import socket

url=input('Enter your url:')
words=url.split('/')
host=words[2]


mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect((host,80))
mysock.send(('GET '+ url+' HTTP/1.0\r\n\r\n').encode())

while(True):
    data=mysock.recv(512)
    if (len(data)<1):
        break
    print(data.decode())
mysock.close()    
