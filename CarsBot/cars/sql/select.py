import sqlite3

async def get_all_products(chat_id: int):
    conn = sqlite3.connect("shop.db")
    cursor = conn.cursor()

    query = f"select * from cars where chat_id={chat_id}"
    cars = cursor.execute(query).fetchall()
    return cars