def sort_by_len(element: str) -> int:
    return len(element)


sort_by_len_lambda = lambda element: len(element)

print(sort_by_len_lambda("banana"))

fruits = ["banana", "apple", "cherry", "date"]
longest_word = max(fruits, key=lambda element: len(element))
print(longest_word)
