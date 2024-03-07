class Point:
    color = "red"
    circle = 2

    def set_coords(self, x, y):
        self.x = x
        self.y = y
        print(self.__dict__)
        print(self)
        print("Вызов метода set_coords")


print(Point.set_coords)
# Point.set_coords()
pt = Point()
pt.set_coords(10, 30)
print(pt.__dict__)
