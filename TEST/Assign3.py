from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def call(self):
        pass

class Circle(Shape):
    def test(self):
        print("test")

    def call(self):
        pass

cc=Circle()
cc.test()
