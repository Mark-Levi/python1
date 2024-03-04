squares = []
for x in range(10):
    squares.append(x**2)
print(squares)
squares2 = [x**2 for x in range(10)]
print(squares)
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)
numbers = [1, 2, 3, 4, 5]
labeled_numbers = ["even" if num % 2 == 0 else "odd" for num in numbers]
print(labeled_numbers)
square_dict = {x: x**2 for x in range(10)}
print(square_dict)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transpose_matrix = [[row[i] for row in matrix] for i in range(len(matrix))]
print(transpose_matrix)
