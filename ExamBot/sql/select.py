import sqlite3

async def select_user(chat_id: int):
    conn = sqlite3.connect('exam.db')
    cursor = conn.cursor()

    user = query = f'select * from users where chat_id={chat_id}'
    cursor.execute(query).fetchone()
    return user 



async def select_car(chat_id: int):
    conn = sqlite3.connect('exam.db')
    cursor = conn.cursor()

    query = f'select * from cars where chat_id={chat_id}'
    cursor.execute(query)
    cars = cursor.fetchall()

    conn.close()
    return cars
