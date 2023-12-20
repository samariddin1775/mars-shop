import sqlite3

conn = sqlite3.connect("cars.db")
cursor = conn.cursor()

query = """
create table cars(
    id integer primary key autoincrement,
    photo text,
    name text,
    chat_id integer
)
"""

cursor.execute(query)
conn.commit()