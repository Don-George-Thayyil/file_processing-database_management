import csv 

class PhoneContact:
    def __init__(self, name, number):
        self.name = name
        self.number = number
    
class Phone:
    def load_csv(self, name):
        self.contacts = []
        with open(name, newline="") as file:
            read = csv.DictReader(file)
            for i in read:
                arr = {i["Name"]:i["Number"]}
                self.contacts.append(arr)
        
    
    def search_for(self,value):
        final = []
        self.value = value.lower()
        for item in self.contacts:
            for key, value in item.items():
                if self.value in key.lower():
                    final.append(item)
        if len(final) != 0:
            return final
        return False

    def search(self, name):
        if self.search_for(name.lower()) == False:
            print("Nothing")
        else:
            for item in self.search_for(name.lower()):
                for key, value in item.items():
                    print(key, " : ", value)
    
    def write(self):
        with open("contacts.csv", "a", newline = "") as file:
            while 1:
                self.ip_name = input("enter the name: ")
                self.ip_numb = input("enter the number: ")
                write = csv.writer(file, delimiter = ",")
                write.writerow([self.ip_name, self.ip_numb])
                if input("exit(y): ") == "y":
                    break

c = Phone()

c.load_csv("contacts.csv")

c.search("no")
c.write()
c.search("ar")
