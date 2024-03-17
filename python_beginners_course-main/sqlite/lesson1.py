import sqlite3 as sq

# con = sq.connect("saper.db")
# cur = con.cursor()
# cur.execute("""""")
# con.close()

# При работе через менеджера база закрывается автоматически
with sq.connect("saper.db") as con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS games")
    cur.execute(
        """CREATE TABLE IF NOT EXISTS games (
                game_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                time INTEGER,
                score INTEGER)"""
    )
