class Mother:
    def call(self):
        print("mother")

class Father:
    def call(self):
        print("father")

class Child(Mother,Father):
    def call(self):
        print("child")

c=Child()
c.call()
