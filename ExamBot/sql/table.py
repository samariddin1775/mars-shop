import sqlite3 

conn = sqlite3.connect('exam.db')
cursor = conn.cursor()


query = """
CREATE TABLE users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    photo TEXT,
    chat_id INTEGER  
)
"""
cursor.execute(query)
conn.commit()