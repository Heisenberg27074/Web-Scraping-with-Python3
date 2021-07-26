
count=0
fname=input("Enter your file name:")
fh=open(fname)
for line in fh:
    if not line.startswith('From '):
        continue
    else:
        word=line.split()
        print(word[1])
        count=count+1
print("There were", count, "lines in the file with From as the first word")