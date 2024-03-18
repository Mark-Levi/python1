import re

text = "Карта map и объект bitmap - это разные вещи"

# match = re.findall("map", text)
match = re.findall(r"\bmap\b", text)
print(match)
tex = "Еда, еду, победа"
match = re.findall(r"[Ее]д[ау]", tex)
print(match)
