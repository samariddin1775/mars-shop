import sqlite3



async def insert_product(data: dict):
    conn = sqlite3.connect("cars.db")
    cursor = conn.cursor()

    chat_id = data.get("chat_id")
    photo = data.get("image")
    name = data.get("name")
    


    query = (f"""insert into products(photo, info, contact, chat_id, price) values ('{photo}', '{name}', {chat_id})""")

    cursor.execute(query)
    conn.commit()

    return True