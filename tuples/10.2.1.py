#Write a program to read through the mbox-short.txt and figure out the distribution by hour of the
# day for each of the messages. You can pull the hour out from the 'From ' line by finding the time
# and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown
# below.
wds=list()
di=dict()
fname=input("enter your file name:")
if len(fname)<1 : fname='mbox-short.txt'
fhand=open(fname)
for line in fhand:
    words=line.split()
    if len(words)<1 or words[0]!='From':
        continue
    else:    
        
        wds.append(words[5])
for w in wds:
    pos=w.find(':')
    hrs=w[pos-2:pos]
    di[hrs]=di.get(hrs,0)+1
#print(di)

#sorting by keys
for k,v in sorted(di.items()):
    print(k,v)
        