class emp:
    def __init__(self,n,s):
        self.name=n
        self.sal=s
    def d(self):
        print("name is "+self.name)
        print("salary is "+str(self.sal))
ob =emp("abc",100)
ob.d()
