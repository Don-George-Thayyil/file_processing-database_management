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
                arr = {i["Name"]:i["Phone"]}
                self.contacts.append(arr)
        
    
    def search(self,value):
        final = []
        self.value = value.lower()
        for item in self.contacts:
            for key, value in item.items():
                if self.value in key:
                    final.append(item)
        if len(final) != 0:
            return final
        return f"No Contacts found"

c = Phone()

c.load_csv("contacts.csv")
for item in c.search("mo"):
    for key, value in item.items():
        print(key, " : ", value)
