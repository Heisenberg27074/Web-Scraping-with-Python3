#Histogram code
fname=input("Enter your file name:")
fhandle=open(fname)
counts=dict()
for line in fhandle:
    words=line.split()
    for word in words:
        #if word in counts:
          # counts[word]=counts[word]+1
        #else:    counts[word]=1 
        counts[word]=counts.get(word,0)+1     
        
print(counts)        
        
        
#larger code
bigword=None
bigcount=None
for word,count in counts.items():
    if bigcount is None or count>bigcount:
        bigcount=count
        bigword=word
print(bigword,bigcount)        
        