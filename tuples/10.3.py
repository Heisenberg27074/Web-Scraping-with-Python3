fname=input("Enter ur file name:")
if len(fname)<1:fname='mbox-short.txt'
counts=dict()
try:
    fhand=open(fname)
except:
    print("File can't be opened:",fname)
for line in fhand:
    if not line.startswith('From '):
        continue
    else:
        words=line.split()
        newwds=words[1]
        atsplit=newwds.split('@')
        piece=atsplit[1]
        counts[piece]=counts.get(piece,0)+1
print(counts)        
        
prosender=None
procount=None
for k,v in counts.items():
    if procount== None or v>procount:            
        procount=v
        prosender=k
print(prosender,procount)        