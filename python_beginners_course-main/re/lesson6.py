import re

text = "+7(123)456-78-90"
m = re.match(r"\+7\(\d{3}\)\d{3}-\d{2}-\d{2}", text)
print(m)

count = 0


def replFind(m):
    global count
    count += 1
    return f"<option value='{count}'>{m.group(1)}</option>\n"


text = """Москва
Казань
Тверь
Самара
Уфа"""
list2 = re.sub(r"\s*(\w+)\s*", replFind, text)
print(list2)
