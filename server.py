import socket
import sqlite3 as sq
import pickle
with sq.connect("users.db") as con:
    cur=con.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Users (
    hash TEXT NOT NULL,
    username TEXT NOT NULL
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
        if data["toHash"] in ['1','2','3']:
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
        print(gd)
        conn.send(pickle.dumps(gd))