import sqlite3

async def delete_cars(cat_id: int):
    conn = sqlite3.connect('exam.db')
    cursor = conn.cursor()

    query = f"delete from cars where id={cat_id}"
    delete = cursor.execute(query)
    conn.commit()
    return delete
