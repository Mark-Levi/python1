import re

text = "Google, Gooogle, Goooooogle"
# Мажорный режим
match = re.findall(r"o{2,5}", text)
print(match)
# Минорный режим
match = re.findall(r"o{2,5}?", text)
print(match)
phone = "89123456789"
match = re.findall(r"8\d{10}", phone)
print(match)
# Второй символ н может быть а может и отсутствавать
text = "стеклянный, стекляный"
match = re.findall(r"стеклянн?ый", text)
print(match)
text = "author=Пушкин А.С.; title = Евгений Онегин; price =200; year= 2001"
match = re.findall(r"\w+\s*=\s*[^;]+", text)
print(match)
