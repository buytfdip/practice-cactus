import sqlite3
import config

connection = sqlite3.connect(config.DB_FILE)

cursor = connection.cursor()

cursor.execute("""
DROP TABLE Phones
""")

connection.commit()