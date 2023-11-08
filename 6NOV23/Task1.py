
class Test:
    num=12
    def __init__(self,num):
        self.num=num
        # print("hello",self.num)

    def __init__(self):

        print("hello")
    def call(self):
        print(self.num)

ab=Test()
bc=Test()
ab.call()
bc.call()

