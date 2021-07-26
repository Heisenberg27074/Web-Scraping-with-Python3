#Histogram code

fname=input("enter your file name:")
if len(fname)<1:    
    fname='clown.txt'
fhand=open(fname)
di=dict()
for line in fhand:
    words=line.split()
    for word in words:
        di[word]=di.get(word,0)+1
        
#print(di)

#sorting by keys
#for k,v in sorted(di.items()):
   # print("Sorted:",k,v)

#sorting by values
tmp=list()
for k,v in di.items():
    
    newtuple=(v,k)
    tmp.append(newtuple)
#print('Flipped', tmp)  

tmp=sorted(tmp, reverse=True)

for v,k in tmp[:10]:

    print(k,v)
