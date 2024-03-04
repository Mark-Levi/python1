# numbers_1 = [1, 2, 3, 4, 5]
# average_1 = sum(numbers_1)/len(numbers_1)
# print(average_1)

# numbers_2 = [11, 12, 13, 14, 15]
# average_2 = sum(numbers_2)/len(numbers_2)
# print(average_2)

# numbers_1 = [1, 2, 3, 4, 5]
# numbers_2 = [11, 12, 13, 14, 15]


# def find_average(numbers):
#     average = sum(numbers)/len(numbers)
#     return average


# # Функция заглушка
# def nothing():
#     pass


# average_1 = find_average(numbers_1)
# print(average_1)


def format_date(*, day: int, month: str) -> str:
    return f"The date is {day} of {month}"


print(format_date(month="October", day=15))
