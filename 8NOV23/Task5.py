class Grand:
    name="grand"
    def call(self):
        print("grand")
    def test(self):
        print("test")
class Inlaw(Grand):
    def call(self):
        print("duaghter in law")
class Son(Grand):
    def call(self):
        print("son")
class Child(Inlaw,Grand):
    age=20

c=Child()
c.call()
c.test()
print(c.name)
print(c.age)
