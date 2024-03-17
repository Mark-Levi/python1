import sqlite3 as sq


with sq.connect("saper.db") as con:
    cur = con.cursor()
    # cur.execute(
    #     """INSERT INTO users (
    #             name,sex,old,score) VALUES("Anna",1,19,300)"""
    # )
    # cur.execute("""SELECT name, old FROM users""")
    # b = cur.fetchall()
    # print(b)
    # cur.execute("""UPDATE users SET score =1000 WHERE user_id >2""")
    # cur.execute("""UPDATE users SET score =score+1500 WHERE name LIKE 'An%'""")
    # cur.execute("""SELECT count(user_id) AS co FROM games WHERE user_id = 1""")
    # b = cur.fetchall()
    # print(b)
    # cur.execute("""SELECT sum(score) AS sum FROM games GROUP BY user_id """)
    # b = cur.fetchall()
    # print(b)
    # cur.execute(
    #     """SELECT name,sex,sum(games.score) AS sum FROM games LEFT JOIN users
    #             ON users.user_id =games.user_id GROUP BY games.user_id """
    # )
    # b = cur.fetchall()
    # print(b)
    # cur.execute(
    #     """SELECT name,subject,mark FROM marks
    #      JOIN students ON students.rowid = marks.id
    #      WHERE mark >
    #      (seLect MARK from MARKS
    #      WHERE id = 2 AND subject LIKE'Си')
    #      AND subject LIKE'Си' """
    # )
    # b = cur.fetchall()
    # print(b)
    cur.execute(
        """INSERT INTO female
          SELECT NULL,name,sex,old FROM students WHERE sex = 2"""
    )
    b = cur.fetchall()
    print(b)
# print(b[0][0])
