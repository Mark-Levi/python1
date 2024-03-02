person = {"name": "John", "age": 30, "city": "New York"}
additional_person_info = {"job": "Engineer", "married": True, "city": "London"}
person["job"] = "Engineer"
# print(person)
# print(person["name"])
# print(person.get("name"))
# print(person.get("sex"))
# print(person.get("sex", "Male"))

# for p in person:
#     print(p)
# for item in person.items():
#     print(item)
#     key, value = item
#     print(value)

# for key, value in person.items():
#     print(value)

# for key in person.keys():
#     print(key)
# for value in person.values():
#     print(value)

# person.update(additional_person_info)
# тот же результат
person = person | additional_person_info
print(person)
