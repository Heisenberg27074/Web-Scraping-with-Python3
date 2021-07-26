#Write a program to read through the mbox-short.txt and figure out who has sent the greatest
# number of mail messages. The program looks for 'From ' lines and takes the second word of those
# lines as the person who sent the mail. The program creates a Python dictionary that maps the 
#sender's mail address to a count of the number of times they appear in the file. After the
# dictionary is produced, the program reads through the dictionary using a maximum loop to find 
#the most prolific committer.


#code for histogram
fname=input("Enter the file name:")
fhnadle=open(fname)
counts=dict()
for line in fhnadle:
    if not line.startswith("From "):
        continue
    else:
        nline=line.split()
        secword=nline[1]
        #for word in nline:
        counts[secword]=counts.get(secword,0)+1
            
            
#code for larger number of mails
procount=None
proname=None
for name,count in counts.items():
    if procount is None or count > procount:
        procount=count
        proname=name
print(proname,procount)        
            
            