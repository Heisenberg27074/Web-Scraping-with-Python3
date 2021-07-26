def counter(strin,lett):
    count=0
    for letter in strin:
        if letter==lett:
            count=count+1
    return(count)
        
        
        
strin = input("enter ur string")
lett  =input("enter letter to be searched")
x=counter(strin,lett)
print("count of" + lett + "in string:",x)    
#x=strin.count('a'[0[10]])
#print(x)