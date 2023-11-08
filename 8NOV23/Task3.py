class Grand:
    def call(self):
        print("grand")
class Father(Grand):
    # def call(self):
        print("father")

class Son(Father):
    # def call(self):
    #     print("son")
    def m1(self):
        print("m1")


s=Son()
s.call()
s.m1()

