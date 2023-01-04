import json
import sqlite3
import config

connection = sqlite3.connect(config.DB_FILE)
cursor = connection.cursor()
cursor.execute('Create Table if not exists Phones (Name Text, Price Interger, Link Text)')

traffic = json.load(open(config.LOG_FILE))
columns = ['Name','Price','Link']
for row in traffic:
    keys= tuple(row[item] for item in columns)
    cursor.execute('insert into Phones values(?,?,?)',keys)
    print(f'{row["Name"]} data inserted Succefully')

connection.commit()
connection.close()