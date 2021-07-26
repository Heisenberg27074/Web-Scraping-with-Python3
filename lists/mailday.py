fname=input("Enter ur file nam,e:")
if len(fname)<1:fname='mbox-short.txt'
fhand=open(fname)
for line in fhand:
    words=line.split()
    if len(words)==0 or len(words)<3:continue
    if words[0]!='From':continue
    else:
        print(words[2])