import sqlite3

connection = sqlite3.connect("database.db")

cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS people(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    grade TEXT NOT NULL
);""")

values = [("Don",22,"A+"),("Harry",24,"D+"),("Jackson",20,"B+"),("Merin",23,"A+")]
cursor.executemany("INSERT INTO people(name,age,grade) VALUES(?,?,?)",values)
connection.commit()

for row in cursor.execute("SELECT * FROM people"):
    print(row)
