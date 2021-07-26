index=0
st='czeckoslowakia'
while index<len(st): #index<=len(st)-1 /same 
   # print(st[index])
    index=index+1
    
    
    #Write a while loop that starts at the last character in the
#string and works its way backwards to the first character in the string,
#printing each letter on a separate line, except backwards.
 
index=len(st)-1
while index>-1:
    print(st[index])
    index=index-1