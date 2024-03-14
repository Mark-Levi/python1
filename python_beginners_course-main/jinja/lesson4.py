from jinja2 import Environment, FileSystemLoader
import os

persons = [
    {"name": "Алексей", "old": 18, "weight": 78.5},
    {"name": "Николай", "old": 28, "weight": 82.3},
    {"name": "Иван", "old": 33, "weight": 94.0},
]
print(os.getcwd())
file_loader = FileSystemLoader("templates")
env = Environment(loader=file_loader)

print(env.list_templates())
tm = env.get_template("page.htm")
msg = tm.render(users=persons, domain="www.domain.ru", title="Заголовок")

print(msg)
