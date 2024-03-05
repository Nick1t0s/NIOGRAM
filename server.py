import socket
import sqlite3 as sq
import pickle
def chechHash(hash):
    with sq.connect("users.db") as con:
        cur = con.cursor()
        cur.execute(f"SELECT 1 FROM Users WHERE hash='{hash}' LIMIT 1")
        res = bool(cur.fetchall())
    return res
with sq.connect("users.db") as con:
    cur=con.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS users (
    hash TEXT NOT NULL,
    password TEXT NOT NULL
    )
    ''')
with sq.connect("messages.db") as con:
    cur=con.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS messages (
    fromHash TEXT,
    toHash TEXT,
    text TEXT,
    ttg INTAGER
    )
    ''')
sock = socket.socket()
sock.bind(('0.0.0.0', 9090))
sock.listen(1)
while True:
    conn, addr = sock.accept()
    data = pickle.loads(conn.recv(1024))
    if data["type"]=="send":
        if data["toHash"] in ['@1','@2','@3']:
            conn.send("done".encode())
            print(data)
            with sq.connect("messages.db") as con:
                cur=con.cursor()
                print(f"INSERT INTO messages VALUES({data['fromHash']}, {data['toHash']}, '{data['text']}', 0)")
                cur.execute(f"INSERT INTO messages VALUES('{data['fromHash']}', '{data['toHash']}', '{data['text']}', 0)")
        else:
            conn.send("noUser".encode())
    elif data["type"]=="get":
        with sq.connect("messages.db") as con:
            cur=con.cursor()
            cur.execute(f"SELECT * FROM messages WHERE ttg = 0 AND toHash='{data['fromHash']}'")
            print(f"SELECT * FROM messages WHERE ttg = 0 AND toHash='{data['fromHash']}'")
            results = cur.fetchall()
            gd=[]
            print("dn")
        for row in results:
            print(row)
            gd.append(list(row))
        with sq.connect("messages.db") as con:
            cur=con.cursor()
            cur.execute(f"UPDATE messages set ttg=1 WHERE ttg = 0 AND toHash='{data['fromHash']}'")
    elif data["type"]=="checkHash":
        print("checkHash")
        if chechHash(data["hash"]):
            conn.send("1".encode())
            print("1")
        else:
            conn.send("0".encode())
        print(str(int(chechHash(data["hash"]))))
        print("endReg")
    elif data["type"]=="RegUser":
        print("reg")
        if chechHash(data["hash"]):
            print("hashErr")
            conn.send("hashErr".encode())
        else:
            with sq.connect("users.db") as con:
                cur=con.cursor()
                cur.execute(f"INSERT INTO users VALUES('{data['hash']}', '{data['pass']}')")
            conn.send("done".encode())
            print("done")