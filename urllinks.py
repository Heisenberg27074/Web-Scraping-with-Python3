# Retreivinglinl from a website while the count of links to retreive links will be inputted by user and the position of link to retreive must also be given by user.



import urllib.request, urllib.parse, urllib.error

#using beautiful soup library to parse html beautifully
from bs4 import BeautifulSoup
import ssl

#Ignore SSL Certificates
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url=input('Enter url:')
pos=int(input('Enter position:'))-1
count=int(input('Enter no. of reps:'))

fhand=urllib.request.urlopen(url,context=ctx).read()
soup=BeautifulSoup(fhand,'html.parser')
tags=soup('a')


for c in range(count):
    link=tags[pos].get('href',None)
    x=tags[pos].contents[0]
    print('Retreiving link:',link)
    fhand=urllib.request.urlopen(link,context=ctx).read()
    soup=BeautifulSoup(fhand,'html.parser')
    tags=soup('a')
    #print(tags[pos].get('href',None))
print(x)    
