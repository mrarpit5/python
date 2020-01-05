class se:
    def __init__(self):
        self.x=10
    def m(self):
        self.x=input("enter x ")
s=se()
s2=se()
print("x is",s.x)
print("x2 is",s2.x)
s.m()
print("s1",s.x)
print("s2",s2.x)
