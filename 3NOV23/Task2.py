class Person:
    name = None
    age = None
    address = None

    def eat(self):
        print("eat")

    def sleep(self):
        print("sleep")

    def repeat(self):
        print("Name = ", self.name)
        print("Age = ", self.age)
        print("Address = ", self.address, "\n")


ram_obj = Person()
ram_obj.name = input("enter name : ")
ram_obj.age = input("enter age : ")
ram_obj.address = input("enter address : ")

sam_obj = Person()
sam_obj.name = input("\nenter name : ")
sam_obj.age = input("enter age : ")
sam_obj.address = input("enter address : ")

print("**************==Output==******************")
sam_obj.repeat()
ram_obj.repeat()

# print(sam_obj.name,sam_obj.age,sam_obj.address)
