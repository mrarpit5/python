class Person:
    def Person():
        name = input("Enter name : ")
        weight = int(input("Enter weight : "))
        height = int(input("Enter height : "))
        bm = weight/(height*height)
        print("Bodymass : ",bm)
        if(weight < 20):
            print("Underweight")
        elif(weight > 20 and weight < 25):
            print("Appropriate weight")
        elif(weight > 25 and weight < 30):
            print("Overweight")
        elif(weight > 30 and weight < 39):
            print("Obese")
Person.Person()
