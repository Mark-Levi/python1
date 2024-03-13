from string import ascii_letters


class Person:

    S_RUS = "абвгдеёжзиклмнопрстуфхцчшщьъэюя-"
    S_RUS_UPPER = S_RUS.upper()

    def __init__(self, fio, old, ps, weight):
        self.verify_fio(fio)
        self.verify_old(old)
        self.verify_weight(weight)
        self.verify_ps(ps)

        self.__fio = fio.split()
        self.__old = old
        self.__passport = ps
        self.__weight = weight

    @classmethod
    def verify_fio(cls, fio):
        if type(fio) is not str:
            raise TypeError("ФИО должно бытьстрокой")
        f = fio.split()
        if len(f) != 3:
            raise TypeError("Неверный формат ФИО")
        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER
        for s in f:
            if len(s) < 1:
                raise TypeError("В каждой части ФИО должен быть >1 символ ")
            if len(s.strip(letters)) != 0:
                raise TypeError("Недопустимый символ в ФИО")

    @classmethod
    def verify_old(cls, old):
        if type(old) is not int or old < 14 or old > 120:
            raise TypeError("Возраст должен быть целым числом от 14 до 120")

    @classmethod
    def verify_weight(cls, weight):
        if type(weight) is not float or weight < 20:
            raise TypeError("Возраст должен быть числом float больше 19")

    @classmethod
    def verify_ps(cls, ps):
        if type(ps) is not str:
            raise TypeError("Номер паспорта  должно быть строкой")
        s = ps.split()
        if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
            raise TypeError("Неправильный формат номера паспорта")
        for p in s:
            if not p.isdigit():
                raise TypeError("В номере паспорта должны быть только цифры")

    @property
    def fio(self):
        return self.__fio

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.verify_old(old)
        self.__old = old


p = Person("Иванов Иван Fox", 30, "1234 555555", 80.0)
p.old = 45
print(p.__dict__)
