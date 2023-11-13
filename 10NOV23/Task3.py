from abc import ABC, abstractmethod


class Person(ABC):
    @abstractmethod
    def call(self):
        pass

    def test(self):
        print("test")


class AB(Person):
    def call(self):
        super().test()
        print("AB speak")


class BC(Person):
    def call(self):
        super().test()
        print("speak BC")


aa = AB()
aa.call()

bb = BC()
bb.call()