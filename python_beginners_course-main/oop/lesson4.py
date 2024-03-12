class Point:
    def __new__(cls, *args, **kwargs):
        print("Вызов __new__для " + str(cls))
        return super().__new__(cls)  # Без этого не создается экземпляр класса

    def __init__(self, x=0, y=0):
        print("Вызов __init__ для " + str(self))
        self.x = x
        self.y = y


pt = Point(1, 2)


# Паттерн Singleton
# Может создаваться только один экземпляр класса
class Database:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        Database.__instance = None

    def __init__(self, user, psw, port) -> None:
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f"Соединение с БД: {self.user}, {self.psw}, {self.port}")

    def close(self):
        print("Закрытие соединения с БД")

    def read(self):
        print("Чтените данных из БД")

    def write(self, data):
        print(f"Запись данных в БД {data}")


db = Database("root", "1234", "80")
db2 = Database("root2", "12342", "802")

print(id(db), id(db2))
print(db2.user)
