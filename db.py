import sqlite3

conn = sqlite3.connect('database.db')
print("Opened database successfully")

conn.execute('CREATE TABLE picture (id Integer PRIMARY KEY autoincrement, p_name NVARCHAR(40))')
print("Table created successfully")
conn.close()