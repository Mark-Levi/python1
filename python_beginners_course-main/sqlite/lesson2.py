import sqlite3 as sq


with sq.connect("saper.db") as con:
    cur = con.cursor()
    # cur.execute(
    #     """INSERT INTO users (
    #             name,sex,old,score) VALUES("Anna",1,19,300)"""
    # )
    cur.execute("""SELECT name, old FROM users""")
    b = cur.fetchall()
    print(b)
print(b[0][0])
