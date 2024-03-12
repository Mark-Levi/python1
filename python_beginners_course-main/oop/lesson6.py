# Инкапсуляция
class Point:
    def __init__(self, x=0, y=0) -> None:
        self.__x = x
        self.__y = y

    def get_coord(self):
        return self.__x, self.__y


pt = Point(1, 2)
a = pt.__x
# pt.x = 200
# pt.__y = "Fill"
print(pt.__dict__)
print(pt.get_coord())
