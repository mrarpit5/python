from abc import ABC
class a(ABC):
    def dis():
        pass
class demo(a):
    def dis(self):
        print("abstract class demo")
ob=demo()
ob.dis()
