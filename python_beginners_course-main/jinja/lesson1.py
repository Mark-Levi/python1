from jinja2 import Template

# name = "Федор"

# tm = Template("Привет {{name}}")
# msg = tm.render(name=name)
# print(msg)

# data = """{% raw%} Модуль Jinja вместо
# определения {{name}}
# подставляет соответствующее значение {% endraw %}"""
# t2 = Template(data)
# msg = t2.render(name="Jhon")
# print(msg)

# # Экранирование ссылок
# link = """В HTML документе ссылки определяются так;
# <a href = "#">Ссылка </a>"""
# t3 = Template("{{link | e}}")
# msg = t3.render(link=link)
# print(msg)
# # Вариант экранирования 2
# # msg = escape(link)
# # print(msg)
# # Не работает в новой версии jinja

cities = [
    {"id": 1, "city": "Москва"},
    {"id": 2, "city": "Клин"},
    {"id": 3, "city": "Минск"},
]
link = """ <select name = "cities">
{% for c in cities -%}
{% if c.id <= 2 -%}
   <option value="{{c["id"]}}">{{c["city"]}}</option>
{% endif -%}
{% endfor -%}
</select>"""

tm = Template(link)
msg = tm.render(cities=cities)
print(msg)
