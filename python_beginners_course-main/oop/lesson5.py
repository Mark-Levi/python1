class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    def __init__(self, x, y):
        self.x = self.y = 0
        if Vector.validate(x) and self.validate(
            y
        ):  # Можно обращаться как по имени класса так и экземпляра класса
            self.x = x
            self.y = y

    def get_coord(self):
        return self.x, self.y

    @staticmethod  # Не связан с объектами и методами класса
    def norm2(x, y):
        return x * x + y * y


v = Vector(1, 2)
res = v.get_coord()
res2 = Vector.get_coord(v)
x, y = res2
print(x, y)
print(Vector.validate(120))
print(Vector.norm2(5, 6))
