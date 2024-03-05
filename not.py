import sqlite3 as sq
with sq.connect("messages.db") as con:
    cur=con.cursor()
    cur.execute("SELECT 1 FROM messages WHERE toHash='2' LIMIT 1")
    res=bool(cur.fetchall())
    print(res)