# Inheritance



# Single inheritance
class Person: # parent class
    def __init__(self,fname, lname):
        self.firstname = fname
        self.lastname = lname
    
    def printname(self):
        print(f"{self.firstname} {self.lastname}")

    def isStudent(self):
        return False

class Student(Person): # child class or person class

    def isStudent(self):
        return True
class Grades:
    def __init__(self,math, science, english):
        self.mathGrade =math
        self.englishGrade = english
        self.scienceGrade = science

    def printGrade(self):
        print(f"{self.mathGrade} {self.scienceGrade} {self.englishGrade}")


# Multilevel inheritance



# Multiple inheritance
class studentRecord(Person,Grades):
    def __init__(self,fname,lname,math,english,science):
        self.firstname = fname
        self.lastname = lname
        self.math_Grade = math
        self.english_Grade = english
        self.science_Grade = science
    
    def printname(self):
        print(f"\n{self.firstname}\n{self.lastname}\n{self.math_Grade}\n{self.english_Grade}\n{self.science_Grade}")

# 

person1 = Person("julen", "Dio")
person1.printname()
print(f"Student? {person1.isStudent()}")

person2 = Student("julien", "Dio")
person2.printname()
print(f"Student? {person1.isStudent()}")

person1 = studentRecord("julien", "Dio", 80, 80, 90)
person1.printname()