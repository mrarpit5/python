class p:
    def __init__(self,na,no):
        self.name=na
        self.number=no
    def pr(self):
        print("name is "+self.name)
        print("number is "+str(self.number))
class c(p):
    pass

ob=c("abc",1)
ob.pr()
