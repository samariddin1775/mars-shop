import sqlite3

async def insert_user(data: dict):
    conn = sqlite3.connect('exam.db')
    cursor = conn.cursor()


    name = data.get('name')
    phone = data.get('phone')
    chat_id = data.get('chat_id')

    query = (f"""insert into users (name, phone, chat_id) 
             values('{name}','{phone}', {chat_id})""")
    
    cursor.execute(query)
    conn.commit()
    return True


async def insert_car(data: dict):
    conn = sqlite3.connect('exam.db')
    cursor = conn.cursor()

    name = data.get('name')
    photo = data.get('photo')
    chat_id = data.get('chat_id')

    query = (f"""insert into cars (name, photo, chat_id) 
             values('{name}','{photo}', {chat_id})""")
    
    cursor.execute(query)
    conn.commit()
    return True

