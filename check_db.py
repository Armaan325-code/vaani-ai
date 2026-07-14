import sqlite3
conn = sqlite3.connect("vaani.db")
cursor = conn.cursor()

cursor.execute("select*FROM users")
rows = cursor.fetchall()
print(rows)
conn.close()