class sam:
    x=10
    def m(cls):
        cls.x=11
s1=sam()
s2=sam()

print(s1.x)
print(s2.x)
s1.m()
print(s1.x)
print(s2.x)
