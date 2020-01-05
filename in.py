class person:
    def __init__(self,name,age):
        self.nam=name
        self.ag=age
    def dis(self):
        return self.nam + " " +self.ag

class stud(person):
    def __init__(self,name,age,city):
        person.__init__(self,name,age)
        self.cit=city
    def Getd2(self):
        return self.dis() + "," +self.cit
a=person("arpit","20")
b=stud("arpit","20","jam")
print(a.dis())
print(b.Getd2())

        
        
