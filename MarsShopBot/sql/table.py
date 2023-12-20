import sqlite3

conn = sqlite3.connect("shop.db")
cursor = conn.cursor()

query = """
create table products(
    id integer primary key autoincrement,
    photo text,
    info text,
    price real,
    chat_id integer,
    contact text
)
"""

cursor.execute(query)
conn.commit()