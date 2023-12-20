import sqlite3


async def update_photo(data: dict):
    conn = sqlite3.connect("cars.db")
    cursor =conn.cursor()


    photo = data.get("photo")
    product_id = data.get("id")


    query = f"update cars set photo='{photo}' where id={product_id}"
    update = cursor.execute(query)

    conn.commit()
    return update