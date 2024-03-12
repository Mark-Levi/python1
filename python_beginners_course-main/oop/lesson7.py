from typing import Any


class Point:
    MIN_COORD = 0
    MAX_COORD = 100

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        if self.MIN_COORD <= x <= self.MAX_COORD:
            self.x = x
            self.y = y

    # def set_bound(self, left):
    #     self.MIN_COORD = left # создается новый аттрибут в э
    # кземпляре, а е перез в классе

    # Правильно делать так
    @classmethod
    # создается новый аттрибут в экземпляре, а не перез в классе
    def set_bound(cls, left):
        cls.MIN_COORD = left

    def __getattribute__(self, item) -> Any:
        # Срабатывает при обращении к любому аттрибуту
        print("__getattribute__")
        if item == "x":
            raise ValueError("Доступ запрешен")
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        # Запрет на создание атрибута с именем Z
        if key == "z":
            raise AttributeError("Недопустимое имя аттрибута")
        else:
            object.__setattr__(self, key, value)

    def __getattr__(self, item):
        print("Оюбращение к несуществующему аттрибуту")
        return False


p = Point(1, 2)
p.set_bound(25)
# print(Point.__dict__)
# a = p.x
print(p.l)
