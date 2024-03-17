import sqlite3 as sq


cars = [
    ("Audi", 56345),
    ("Mersedes", 57800),
    ("Skoda", 9000),
    ("Volvo", 29000),
    ("Bentley", 350000),
]

# При работе через менеджера база закрывается автоматически
with sq.connect("cars.db") as con:
    cur = con.cursor()
    cur.execute(
        """CREATE TABLE IF NOT EXISTS users (
               name TEXT,
               ava BLOB,
               score INTEGER)"""
    )

    # cur.executemany("INSERT INTO cars VALUES(NULL, ?, ?)", cars)
    cur.execute("SELECT model, price FROM cars")
    # c = cur.fetchall()
    # print(c)
    for result in cur:
        print(result[0])
