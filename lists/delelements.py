#Write a function called chop that takes a list and modifies
#it, removing the first and last elements, and returns None. Then write
#a function called middle that takes a list and returns a new list that
#contains all but the first and last elements.

def chop(list1):
    del list1[0]
    del list1[-1]

def middle(list2):
    del list2[-1]
    nlist=list2[1:]
    return(nlist)

list1=[1,2,3,4]
list2=[1,2,3,4]
chop(list1)
print(list1)
x=middle(list2)
print(x)
