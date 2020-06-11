@Imorting urllib modules

import urllib.request, urllib.parse, urllib.error
url=input('Enter')

#urllib.request() is used for requesting a URL and urlopen() for opening a new URL
#fhand is url handle here as in files it was file handle
#Here we do not write encode() as urllib.request.urlopen() does it automatically
fhand=urllib.request.urlopen(url)

#traversing through lines
for line in fhand :
    #decode is used as the file we requested is coming fro outside the world
    #strip() method to remove whitespaces from line
    print(line.decode().strip())
