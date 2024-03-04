# file_names = ["document1.txt", "image1.jpg", "document2.txt", "image2.jpg"]
# for file_name in file_names:
#     print(file_name)
# greeting = "Hello, word!"
# count_o = 0
# for char in greeting:
#     if char == "o":
#         count_o += 1
#         print(char)
# print(count_o)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# for num in numbers:
#     # if num % 2 == 0:
#     #     continue
#     if num == 6:
#         break
#     print(num)
# range_object = range(10, 1, -1)
# print(range_object)
# numbers = list(range_object)
# print(numbers)
numbers = [10, 11, 12, 13, 14, 15]
for i in range(len(numbers)):
    numbers[i] += 1
print(numbers)
