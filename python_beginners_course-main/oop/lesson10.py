from string import ascii_letters


class Person:

    S_RUS = "абвгдеёжзиклмнопрстуфхцчшщьъэюя-"
    S_RUS_UPPER = S_RUS.upper()

    def __init__(self, fio, old, ps, weight):
        self.verify_fio()
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
