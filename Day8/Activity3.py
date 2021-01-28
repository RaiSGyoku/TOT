try:
    class Students:
        def __init__(self, name, mathG, englishG, scienceG):
            self.Student_name = name
            self.Student_English_Grade = englishG
            self.Student_Science_Grade = scienceG
            self.Student_Math_Grade = mathG

        def compute(self):
            average = ( int(self.Student_English_Grade) + int(self.Student_Math_Grade) +int(self.Student_Science_Grade) ) /3
            if average >= 75:
                return (f"{average} Passed")
            else:
                return (f"{average} Failed")

        def displayAll(self):
            print(f"Name: {self.Student_name}\nMath: {self.Student_Math_Grade}\nEnglish: {self.Student_English_Grade}\nScience: {self.Student_Science_Grade}\nAverage: {obj.compute()}")    
    
    inpName = input("Enter Student Name: ")
    inpMathGrade = input("Enter Math Grade: ")
    inpScienceGrade = input("Enter Science Grade: ")
    inpEnglishGrade = input("Enter English Grade: ")
    print("=============================")

    obj = Students(inpName, inpMathGrade, inpScienceGrade, inpEnglishGrade)
    obj.displayAll()
except :
    print("Invalid input")