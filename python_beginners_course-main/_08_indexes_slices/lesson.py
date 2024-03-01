fruits = ["apple", "banana", "cherry", "watermelon"]
print(fruits[0])
print(fruits[-4])
fruits[0] = "tree"
print(fruits)
fruits[0], fruits[3] = fruits[3], fruits[0]
print(fruits)
# Слайсы
numbers = [0, 1, 99, 3, 4, 5, 6, 7, 8, 9]
print(numbers[2:5])
print(numbers[0:10:2])
string = "Africa"
print(string[::2])
