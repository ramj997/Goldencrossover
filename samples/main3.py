
from abc import ABC, abstractmethod
class weapon:
    var=10
    @abstractmethod
    def attack(self):
        var=100
        self.var=var
        return self.var
    @classmethod
    def clsmeth(cls):
        print(cls.var)
        print("class method")
    @staticmethod
    def stmeth():
        # print(var)
        print("static method")

weapon.clsmeth()
w=weapon()
print(weapon.var)
print(w.attack())






