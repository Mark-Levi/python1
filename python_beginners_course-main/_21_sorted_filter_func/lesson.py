# fruits = ["banana", "apple", "cherry", "date"]
# sorted_fruits = sorted(fruits)
# print(sorted_fruits)
# sorted_fruits = sorted(fruits, reverse=True)
# print(sorted_fruits)


# def sort_by_len(element: str) -> int:
#     return len(element)


# sorted_fruits = sorted(fruits, key=sort_by_len)
# print(sorted_fruits)

# people = [
#     {"name": "Alice", "age": 25},
#     {"name": "Bob", "age": 20},
#     {"name": "Diana", "age": 30},
#     {"name": "Charlie", "age": 30},
# ]


# def sort_by_age_name(person: dict) -> tuple[int, str]:
#     return person["age"], person["name"]


# sorted_people = sorted(people, key=sort_by_age_name)
# print(sorted_people)


def is_even(n: int) -> bool:
    return n % 2 == 0


numbers = [1, 2, 3, 4, 5, 6]
filtered_number = list(filter(is_even, numbers))
print(filtered_number)
