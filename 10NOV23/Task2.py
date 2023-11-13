# method overloading

class Test:
    def test(self,a=1,b=1,c=1):
        print(a*b*c)


tt=Test()
tt.test()
tt.test(2,3)
tt.test(2,4,5)