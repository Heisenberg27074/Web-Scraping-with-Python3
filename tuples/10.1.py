#Write a program to read through the mbox-short.txt and figure out the distribution by hour of the
# day for each of the messages. You can pull the hour out from the 'From ' line by finding the time
# and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown
# below.
counts=dict()
fname=input("Enter your file name:")

if len(fname)<1: fname='mbox-short.txt'
fhand=open(fname)
for line in fhand:
    if not line.startswith('From '):
        continue
    else:
        words= line.split()
        newwds=words[5].split(':')
        #print(newwds)
        hrs=newwds[0]
        #print(hrs)
        counts[hrs]=counts.get(hrs,0)+1
#print(counts)
for h,c in sorted(counts.items()):
    print(h,c)
        