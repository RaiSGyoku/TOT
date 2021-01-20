Name = input('Enter Full Name: ')
MathGrade = float(input('Enter Math Grade: '))
ScienceGrade = float(input('Enter Science Grade: '))
EnglishGrade = float(input('Enter English Grade: '))

Average = (float(MathGrade) + float(ScienceGrade) + float(EnglishGrade)) / 3

if Average >= 75:
    if MathGrade <= 74 and EnglishGrade <= 74: 
        print(f'Average:  {Average : .2f}')
        print('Message: ' + "Congratuations! you Passed the Semester. But you need to re-enroll Math and English Subject")
    elif MathGrade <= 74 and ScienceGrade <= 74:
        print(f'Average:  {Average : .2f}')
        print('Message: ' + "Congratuations! you Passed the Semester. But you need to re-enroll Math and Science Subject")
    elif EnglishGrade <= 74 and ScienceGrade <= 74:
        print(f'Average:  {Average : .2f}')
        print('Message: ' + "Congratuations! you Passed the Semester. But you need to re-enroll Science and English  Subject")
        
    elif EnglishGrade <= 74:
        print(f'Average:  {Average : .2f}')
        print('Message: ' + "Congratuations! you Passed the Semester. But you need to re-enroll English Subject")
    elif ScienceGrade <= 74:
        print(f'Average:  {Average : .2f}')
        print('Message: ' + "Congratuations! you Passed the Semester. But you need to re-enroll Science Subject")
    elif MathGrade <= 74:
        print(f'Average:  {Average : .2f}')
        print('Message: ' + "Congratuations! you Passed the Semester. But you need to re-enroll Math Subject")
    

elif Average <= 74:
    print(f'Average:  {Average : .2f}')
    print('Message: ' + "Failed this Semester. you re-enroll all subjects")

else:
    print("Please Enter the Actual Grade")