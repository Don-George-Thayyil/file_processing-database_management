import sqlite3


class Person:
    def __init__(self):
        self.connection = sqlite3.connect("database.db")
        self.cursor = self.connection.cursor()
        self.create_table()
    
    def create_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS new_table(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            grade TEXT NOT NULL
        );""")
    
    def input_text(self):
        while 1:
            self.temp = input("Enter the Text: ")
            if len(self.temp) == 0 or self.temp.isdigit() or self.temp.isspace():
                print("Incorrect input")
                pass
            else:
                return self.temp

    def input_age(self):
        while 1:
            self.temp = input("Enter the age: ")
            if self.temp.isdigit():
                self.temp = int(self.temp)
                if self.temp < 0:
                    print("Age must not be a negative value")
                    pass
                else:
                    return self.temp

    def add_people(self):
        self.name = self.input_text()
        self.age = self.input_age()
        self.grade = self.input_text()
        self.cursor.execute("INSERT INTO new_table(name, age, grade) VALUES(?,?,?)",(self.name, self.age, self.grade))
        self.connection.commit()
        print("Upload completed")

    def show_people(self):        
        for row in self.cursor.execute("SELECT * FROM new_table"):
            print(row)


if __name__ == "__main__":
    person = Person()
    person.create_table()
    for i in range(3):
        person.add_people()
    person.show_people()