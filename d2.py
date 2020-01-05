class person:
    def __init__(self,name,age):
                 self.name = name
                 self.age = age
    def fun(self):
                 print("name is "+self.name)
                 print("age is ",self.age)
ob = person("arpit",20)
ob.fun()
