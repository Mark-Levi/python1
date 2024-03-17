import sqlite3 as sq

cars = [
    ("Audi", 56345),
    ("Mersedes", 57800),
    ("Skoda", 9000),
    ("Volvo", 29000),
    ("Bentley", 350000),
]
# При работе через менеджера база закрывается автоматически
con = None
try:
    con = sq.connect("cars.db")
    cur = con.cursor()
    # cur.execute("DROP TABLE IF EXISTS games")
    cur.execute(
        """CREATE TABLE IF NOT EXISTS cars (
               car_id INTEGER PRIMARY KEY AUTOINCREMENT,
               model TEXT,
               price INTEGER)"""
    )

    cur.executemany("INSERT INTO cars VALUES(NULL, ?, ?)", cars)
    con.commit()

except sq.Error as e:
    if con:
        con.rollback()
    print("Ошибка выполнения запроса")
finally:
    if con:
        con.close()
    # for car in cars:
    #     cur.execute("INSERT INTO cars VALUES(NULL, ?, ?)", car)

# with автоматически запускает по завершению работы
# con.commit() - сохранение всех внесенных изменений в базу
# con.close() - закрытие соединения с БД
