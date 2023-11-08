class Person:
    def __init__(self):
        self.public=10
        self._pro=20
        self.__private=30


    def setv(self):
        self.__private=69

    def getv(self):
            return self.__private

    def call(self):
        pass

man=Person()
man.setv()
print(man.getv())


