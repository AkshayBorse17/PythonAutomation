# Polymorphism & method overriding
class Shape:
    def area(self):
        
        print("area of shapes")


class Rect(Shape):
    def __init__(self,l,w):
        self.l=l
        self.w=w
    def area(self):
        super().area()
        return self.l*self.w

class Circle(Shape):
    def __init__(self,r):
        self.r=r
    def area(self):
        super().area()
        return 22/7*self.r**2

rr=Rect(3,5)
print(rr.area())

cc=Circle(2)
print(cc.area())