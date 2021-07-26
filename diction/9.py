


st=input('Enter anything u want to:')
di=dict()
for something in st:
    #if something not in di:
     #   di[something]=1
    #else:
     #   di[something]=di[something]+1
        di[something]=di.get(something,0)+1

print(di)       

