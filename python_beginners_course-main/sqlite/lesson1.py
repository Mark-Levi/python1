import sqlite3 as sq

# con = sq.connect("saper.db")
# cur = con.cursor()
# cur.execute("""""")
# con.close()

# При работе через менеджера база закрывается автоматически
with sq.connect("saper.db") as con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS users")
    cur.execute(
        """CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                sex INTEGER DEFAULT 1,
                old INTEGER,
                score INTEGER)"""
    )
