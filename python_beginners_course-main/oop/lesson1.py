class Point:
    "Описание класса"
    color = "red"
    circle = 2


a = Point()
b = Point()
a.color = "blue"
Point.color = "Green"
print(a.color)
print(b.color)
print(a.__dict__)

Point.type2 = "Disk"
# The same result
setattr(Point, "type3", "USB")
print(Point.__dict__)
print(
    getattr(Point, "length", "Нет аттрибута")
)  # Обращение к отсутствующему аттрибуту не вызывает ошибки

# Удаление аттрибута класса
print(getattr(Point, "type3", "Нет аттрибута"))
del Point.type3
print(getattr(Point, "type3", "Нет аттрибута"))
# Проверить наличие аттрибута
print(hasattr(Point, "type3"))
# Альтернативный метод
delattr(Point, "type2")

c = Point()
d = Point()
c.x = 1
c.y = 2
d.x = 5
d.y = 6

print(Point.__doc__)
