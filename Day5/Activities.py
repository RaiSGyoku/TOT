class Activity1():
    names = ["Mike","Ana","Jun"]
    englishGrades = [80,78,90]
    sciencehGrades = [80,90,75]
    mathGrades = [90,80,80]


    def student_Averaging(name, mathGrade, englishGrade, scienceGrade):
        Average = (float(mathGrade) + float(scienceGrade) + float(englishGrade)) / 3
        return(f"{name}'s Grade (Math = {mathGrade}, English = {englishGrade}, Science = {scienceGrade}) and Average is {Average: .2f} ")

    a=0   
    for name in names:    
        print(student_Averaging(name, mathGrades[a],englishGrades[a],sciencehGrades[a]))
    a += 1

class Activity2():
    def reverse_Word(inp):
        backwards = inp[::-1]
        return(f'original word: {inp} produced: {backwards} number of character: {len(inp)}')
    print(reverse_Word( inp = input('Enter word here: ')))

