fname=input("Enter your file name:")
fh=open(fname)
for line in fh:
    word=line.split()
    #Guardian a bit stronger
    #if len(line)<3:
        #continue
    
    
    if len(line)<3 or word[0]!= 'From':
        continue
    else:
        print(word[2])