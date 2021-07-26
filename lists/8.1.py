fname=input("enter your file name :")
fhand=open(fname)

lst=list()

for line in fhand:
    word=line.split()
    for piece in word:
        if piece in lst:
            continue
            
        
        else:
            lst.append(piece)
            #print("already exists")
lst.sort()
print(lst)        
