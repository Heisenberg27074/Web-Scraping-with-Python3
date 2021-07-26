class PartyAnimal:
    x=0
    name=""

    def init(self,z):
        self.name=z
        print(self.name,'is constructed')

    def party(self):
        self.x+=1
        print
