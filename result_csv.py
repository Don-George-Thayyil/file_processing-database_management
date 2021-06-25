import csv
import os
from posixpath import relpath

class Result:    
    def make_a_report(self):
        file_name = input("Enter filename: ")
        with open(file_name, "w", newline="") as new_report:
            self.headers = []
            self.col = 0
            while 1:
                self.col += 1
                self.headers.append(input(f"Column {self.col}"))
                if input("press any key to continue or y to Exit: ").lower() == "y":
                    break

            writer = csv.DictWriter(new_report,fieldnames = self.headers)
            writer.writeheader()
    
    def update_report(self):
        file_name = input("file_name: ")
        if os.path.exists(file_name):
            with open(file_name, "a+") as result:
                writer = csv.writer(result, delimiter = ",")
                while 1:
                    self.inputs = []
                    for i in range(len(self.headers)):
                        input_value = input(f"{self.headers[i]}: ")
                        while 1:
                            if len(input_value) != 0:
                                self.inputs.append(input_value)
                                break
                    writer.writerow(self.inputs)
                    if input("exit??: ").lower() == "y":
                        break
        else:
            print("file not found")
            return

    def show(self):
        with open(input("file_name: "),newline="") as result:
            try:
                for item in result:
                    print(item)
            except Exception:
                print("I guess it;s empty :( ")
                

result1 = Result()
# result1.make_a_report()
# result1.update_report()
result1.show()
# new.csv