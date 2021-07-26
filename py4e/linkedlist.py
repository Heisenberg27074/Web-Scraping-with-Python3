class node:
    def ___init___(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def ___init___(self):
        self.start= None

    def traverse(self):
        if self.start==None:
            print('List is empty')
        else:
            temp=self.start
            while temp!= None:
                print(self.data,end=" ")
                temp=temp.next


    def deleteFirst(self):
        if self.start==None:
            print("Linked list is empty")
        else:
            self.start=self.start.next


    def insertLast(self,value):
        new_node=node(value)
        if(self.start==None):
            self.start=new_node;
        else:
            temp=self.start
            while temp.next!=None:
                temp=temp.next
                temp.next=new_node






listlinked=LinkedList()
listlinked.insertLast('10')
listlinked.insertLast('11')
listlinked.insertLast('12')
listlinked.insertLast('13')
listlinked.traverse()
print()
listlinked.deleteFirst()
listlinked.traverse()
