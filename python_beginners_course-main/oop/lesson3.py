class Point:
    color = "red"
    circle = 2

    def __init__(self, x, y) -> None:
        print("Был вызов __init__")
        self.x = x
        self.y = y

    def __del__(self):
        print("Удаление экземпляра класса" + str(self))

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return self.x, self.y


pt = Point(1, 2)
pt2 = Point(5, 7)
pt = 0
print("gggggggggggggg")
print(pt2.__dict__)
