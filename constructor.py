class con:
    def __init__(self):
        print("constructor")
o=con()
    
class c2:
    def __init__(self,n,a):
        self.name=n
        self.age=a
    def p(self):
        print("name is " + self.name)
        print("age is " +str(self.age))
ob=c2("a",1)
ob.p()

class d:
    def __init__(self,na,no):
        self.nam=na
        self.nu=no
    def g(self):
        print("name is "+str(self.nam))
        print("no is "+str(self.nu))
do=d("p",5)
do.g()
