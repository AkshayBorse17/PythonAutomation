class Person:
    def __init__(self):
        self.publicv=10
        self._prov=20
        self.__privatev=30

    def get_pvt(self):
        return self.__privatev

    def set_pvt(self):
        self.__privatev=69
        return self.__privatev

    def publicmethod(self):
        print("public")
        self.__privatemethod()



    def _protectedmethod(self):
        print("protected")
    def __privatemethod(self):
        print("private")


man=Person()
print(man.publicv)
print(man._prov)
man.publicmethod()
man._protectedmethod()

man.get_pvt()
print(man.set_pvt())
