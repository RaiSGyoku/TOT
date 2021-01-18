Name = input('Enter Full Name: ')
MathGrade = input('Enter Math Grade: ')
ScienceGrade = input('Enter Science Grade: ')
EnglishGrade = input('Enter English Grade: ')

Average = (float(MathGrade) + float(ScienceGrade) + float(EnglishGrade)) / 3

# extra
if Average >= 4:
    print('Name: ', Name)
    print('Math Grade: ', MathGrade)
    print('Science Grade: ', ScienceGrade)
    print('EnglishGrade: ',  EnglishGrade)
    print('Average: ', Average)
    print('Status: ' + "Failed")
elif Average <= 3:
    print('Name: ', Name)
    print('Math Grade: ', MathGrade)
    print('Science Grade: ', ScienceGrade)
    print('EnglishGrade: ',  EnglishGrade)
    print('Average: ', Average)
    print('Status: ' + "Pass")
# extra

print('Name: ', Name)
print('Math Grade: ', MathGrade)
print('Science Grade: ', ScienceGrade)
print('EnglishGrade: ',  EnglishGrade)
print('Average: ', Average)
