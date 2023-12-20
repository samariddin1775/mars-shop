import sqlite3



async def insert_product(data: dict):
    conn = sqlite3.connect("shop.db")
    cursor = conn.cursor()

    chat_id = data.get("chat_id")
    photo = data.get("image")
    contact = data.get("contact")
    info = data.get("info")
    price = data.get("price")


    query = (f"""insert into products(photo, info, contact, chat_id, price) values ('{photo}', '{info}', {price}, '{contact}', {chat_id})""")

    cursor.execute(query)
    conn.commit()

    return True
                                                                                     

