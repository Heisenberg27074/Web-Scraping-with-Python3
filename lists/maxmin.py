#Rewrite the program that prompts the user for a list of
#numbers and prints out the maximum and minimum of the numbers at
#the end when the user enters “done”. Write the program to store the
#numbers the user enters in a list and use the max() and min() functions to
#compute the maximum and minimum numbers after the loop completes.

lst=list()
while(1):
    snum=input("Enter a number")
    if snum =='done': break
    try:
        num=float(snum)
        lst.append(num)
    except:print('Please enter a number not anything else!!!')
if len(lst)<1:print("There are no items to compare inside list, please enter some data")
else:    
    print('Maximum:',max(lst))
    print('Minimum',min(lst))    
