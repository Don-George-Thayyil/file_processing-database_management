import sqlite3
from sqlite3.dbapi2 import SQLITE_SELECT


class TodoApp:
    def __init__(self):
        self.connector = sqlite3.connect("todo_data.db")
        self.handler = self.connector.cursor()
        self.welcome()
        self.create_table()
        while(1):
            self.menu()
            self.choose_action()
        
    def welcome(self):
        print("+"+"-"*51+"+")
        print("|"+" "*51+"|")
        print("|"+" "*51+"|")
        print("|"+"WELCOME TO THE TODO APP".center(51)+"|")
        print("|"+" "*51+"|")
        print("|"+" "*51+"|")
        print("+"+"-"*51+"+")
        print()
    
    def menu(self):
        print("1.Display tasks\n2.Add tasks\n3.Change task\n4.Change priority\n5.Delete task\n6.Exit\n")
    
    def choose_action(self):
        while 1:
            x = input("Choose an action (1/2/3/4/5/6): ")
            if self.check_int(x):
                break
            print("Invalid selection choose from (1/2/3/4/5/6)")
        
        if x == "6":
            exit()
        elif x == "1":
            self.show_tasks()
        elif x == "2":
            self.add_tasks()
        elif x == "3":
            self.change_task()
        elif x == "4":
            self.change_priority()
        elif x == "5":
            self.delete_task()

    def create_table(self):
        self.handler.execute("""CREATE TABLE IF NOT EXISTS tasks(
            id INTEGER PRIMARY KEY,
            task TEXT NOT NULL,
            priority INTEGER NOT NULL
        );""")
        self.connector.commit()

    def check_int(self,value):
        temp = value
        if len(temp) == 0:
            return -1
        if temp.isdigit():
            temp = int(temp)
            if temp > 0:
                return True
        return False
    
    def check_string(self, value):
        temp = value
        if len(temp) == 0:
            return -1
        if temp.isdigit() or temp.isspace():
            print("Incorrect input")
            return False
        return True
    
    def check_priority(self, value):
        for row in self.handler.execute("SELECT * FROM tasks"):
            if row[2] == value:
                print(row[2])
                print("Priority can't be overridden !!")
                return False
        return True
        
        
    def input_id(self):
        while 1:        
            id = input("Enter ID to change / press enter to cancel: ")
            if self.check_int(id) == -1:
                return None
            if self.check_int(id):
                return int(id)
    
    def input_text(self):
        while 1:
            temp = input("Enter the Task name: ")
            if self.check_string(temp) == -1:
                return None
            if self.check_string(temp):
                return temp
            

    def input_priority(self):
        while 1:
            temp = input("Enter the priority number: ")
            if self.check_int(temp) == -1:
                return None
            if self.check_int(temp):
                if self.check_priority(int(temp)):
                    return int(temp) 
                return
            print("Invalid number error!!")
            

    def add_tasks(self):
        self.task = self.input_text()
        if self.task != None:
            self.priority = self.input_priority()
            if self.priority != None:
                self.handler.execute("INSERT INTO tasks(task, priority) VALUES(?,?)",(self.task, self.priority))
                self.connector.commit()
                print("Upload completed!!\n")

    def show_tasks(self):
        print()
        print("Table of Tasks".center(80))
        print("--------".center(80))
        hd = ["ID", "TASKS", "PRIORITY"]
        wd = [5, 50, 5]
        print(f"{hd[0].ljust(wd[0])} | {hd[1].ljust(wd[1])} | {hd[2].ljust(wd[2])}")
        print("*"*80)         
        for row in self.handler.execute("SELECT * FROM tasks"):
            print(f"{str(row[0]).ljust(wd[0])} | {row[1].ljust(wd[1])} | {str(row[2]).ljust(wd[2])}")
        print()

    def change_task(self):
        self.id = self.input_id()
        if self.id != None:
            found = False
            for i in self.handler.execute("SELECT id FROM tasks WHERE id = ?",(self.id,)):
                if  i[0] == self.id:
                    found = True
            if found:                    
                self.task = self.input_text()
                if self.task != None:
                    self.handler.execute("UPDATE tasks SET task = ? WHERE id = ?", (self.task, self.id))
                    self.connector.commit()
                    print("Changes commited!!\n")
                return
            print("Incorrect ID")
    
    def change_priority(self):
        self.id = self.input_id()
        if self.id != None:
            found = False
            for i in self.handler.execute("SELECT id FROM tasks WHERE id = ?",(self.id,)):
                if i[0] == self.id:
                    found = True       
            if found:
                self.value = self.input_priority()
                if self.value != None:
                    self.handler.execute("UPDATE tasks SET priority = ? WHERE id = ?", (self.value, self.id))
                    self.connector.commit()
                    print("Changes commited!!\n")
                return
            print("Incorrect ID")

    def delete_task(self):
        self.id = self.input_id()
        if self.id == None:
            return
        found = False
        for i in self.handler.execute("SELECT id FROM tasks WHERE id = ?",(self.id,)):
            if i[0] == self.id:
                found = True
        if found:
            self.handler.execute("DELETE FROM tasks WHERE id = ?", (self.id,))
            self.connector.commit()
            print("Task deleted!!\n")
            return
        print("Incorrect ID")


if __name__ == "__main__":
    def run():
        todo = TodoApp()

run()
