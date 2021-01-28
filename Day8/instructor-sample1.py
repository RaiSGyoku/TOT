# the __init__ function or constructor 
class Employee:
    def __init__(self, name, email):
        self.myname = name
        self.myemail= email

inpName = input("Enter name ")
inpEmail = input("Enter email ")
print("\n")
emp1 = Employee("jasper", "jasper@gmail.com")
emp2 = Employee(inpName, inpEmail)

print (f"employee 1 name {emp1.myname}\nemail {emp1.myemail}\n")
print (f"employee 2 name {emp2.myname}\nemail {emp2.myemail}\n")

