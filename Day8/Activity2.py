class EmployeeInfor:
    def __init__(self, name, email, mobile):
        self.myName = name
        self.myEmail= email
        self.myMobile = mobile

emp1 = EmployeeInfor("Mark", "Mark@gmail.com", 1234534)
emp2 = EmployeeInfor("jasper", "jasper@gmail.com", 4421423)

print (f"employee 1 name: {emp1.myName}\nemail: {emp1.myEmail}\nmobile: {emp1.myMobile}\n")
print (f"employee 2 name: {emp2.myName}\nemail: {emp2.myEmail}\nmobile: {emp2.myMobile}")