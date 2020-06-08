

import socket #socket library imported

 #Creating a socket with web
mysocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# host name & port
host= 'http://web.mit.edu'
port=80

#socket is connected and a tuple is passed containing HOST NAME and PORT
mysocket.connect((host,port)) 

#GET function here to request the host and scrape the webpage we want 
#encode() is used here as it will go on web must be in the right format,
#here no parameter is passed inside encode then it will convert into UTF-8 inside your computer everything is UNICODE.

cmd='GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()

#sending the above command on web as a requese

mysocket.send(cmd)


while True:
    #to receive data, here we will receive first 512 characters
    data=mysocket.recv(512)
    
    #if no data is there simply break
    if len(data)<1:
        break
    
    #decode() is used as data coming from outside world can be in any format(UTF-8,UTF-16 or UTF-32 etc.)
    #so converting it into UNICODE
    print(data.decode())
    
#closing the pathway between web and our program close() method is used    
mysocket.close()    
