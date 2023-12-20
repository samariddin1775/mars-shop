import sqlite3

async def update_photo(data: dict):
    conn = sqlite3.connect('exam.db')
    cursor = conn.cursor()

    photo = data.get('photo')
    product_id = data.get('id')

    query = f"update cars set photo='{photo}' where id={product_id}"
    update = cursor.execute(query)
    conn.commit()
    return update



async def update_name(data: dict):
    conn = sqlite3.connect('exam.db')
    cursor = conn.cursor()

    name= data.get('name')
    product_id = data.get('id')

    query = f"update cars set name='{name}' where id={product_id}"
    update = cursor.execute(query)
    conn.commit()
    return update
