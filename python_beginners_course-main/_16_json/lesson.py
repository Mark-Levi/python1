import json

book = {"title": "1984", "author": "Orwell", "uuid": "kk-234-5"}
json_string = json.dumps(book)
print(json_string)
print(type(json_string))

book_new = json.loads(json_string)
print(book_new)
print(type(book_new))
