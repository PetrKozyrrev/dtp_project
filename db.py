# для работы с базой данных

import sqlite3

conn = sqlite3.connect("dtp_data.db")  # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()

region = "Москва"
datat = "2017"

sql = f"SELECT SUM(dead_count),SUM(injured_count),COUNT(tags) FROM data WHERE region = '{region}' AND datetime LIKE '{datat}%'"
cursor.execute(sql)
a= cursor.fetchall()
print(a[0][1])
