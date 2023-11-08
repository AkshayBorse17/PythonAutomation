
class Person:

    def __init__(self,name,age):
        self.name=name
        self.age=age




name=input("enter name : ")
age=int(input("enter age : "))
man=Person(name,age)
print(man.name,man.age)
