count=0
tot=0.0

inp=input("Enter ur file name:")
fh=open(inp)
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        count=count+1
        cpos=line.find(':')
        nline=line.rstrip()
        snum=nline[cpos+1 : ]
        num=float(snum)
        tot=tot+num
print(count)
print('Average spam confidence:',tot/count)        
        
        