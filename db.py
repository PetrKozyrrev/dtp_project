# для работы с базой данных

import sqlite3

conn = sqlite3.connect("dtp_data.db")  # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()


