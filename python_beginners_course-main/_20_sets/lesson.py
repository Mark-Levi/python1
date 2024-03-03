# Множество (set)
my_set = {1, 2, 3, 4, 5}
print(type(my_set))
print(my_set)
my_set.remove(2)
print(my_set)
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))
# Пересечения
print(set1.intersection(set2))

numbers = [1, 2, 2, 3, 4, 4, 4, 4, 5, 6]
unique_numbers = set(numbers)
print(unique_numbers)
print(list(unique_numbers))
