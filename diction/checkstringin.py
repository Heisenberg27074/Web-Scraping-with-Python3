#Write a program that reads the words in words.txt and stores them as
#keys in a dictionary. It doesn’t matter what the values are. Then you
#can use the in operator as a fast way to check whether a string is in the
#dictionary
fname=input("enter the file name:")
fhand=open(fname)
di=dict()
for line in fhand:
    words=line.split()
    #print(words)
    for word in words:
        di[word]=word
#print("Dictionary",di)  
st=input("Enter the string u want to search")
x=st in di 
print(x)       