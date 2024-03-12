# Свойства property
class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    # Вариант 3
    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.__old = old

    @old.deleter
    def old(self):
        del self.__old

    # old = property(get_old, set_old)
    # Вариант 2
    # old = property()
    # old = old.setter(set_old) # Деккораторы
    # old = old.getter(get_old)


p = Person("Sergey", 20)
# p.set_old(35)
# print(p.get_old())
p.old = 35
print(p.old)
del p.old
print(p.__dict__)
