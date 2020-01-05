from abc import ABC
class ab(ABC):
    def m(n,n2):
        pass
class add(ab):
    def m(self,n,n2):
        a=n+n2
        print("addtion is " ,a)
ob=add()
ob.m(5,5)
