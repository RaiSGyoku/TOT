def Activity1():
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

def Activity2():
    office_name = input('Enter Office Name: ')
    number_Of_Years = input('Enter Number of Years: ')

    IT_Value = 1000
    Accounting_Value = 1200
    HR_Value = 1500

    if (office_name.isalpha() == True and number_Of_Years.isdigit() == True):
        if (office_name.upper() == 'IT' and int(number_Of_Years) >= 10):
            print (IT_Value * 10)
        elif (office_name.upper() == 'IT' and int(number_Of_Years) <= 10):
            print (IT_Value * 5)
        elif (office_name.upper() == 'ACCT' and int(number_Of_Years) >= 10):
            print (Accounting_Value * 10)
        elif (office_name.upper() == 'ACCT' and int(number_Of_Years) <= 10):
            print (Accounting_Value * 5)    
        elif (office_name.upper() == 'HR' and int(number_Of_Years) >= 10):
            print (HR_Value * 10)    
        elif (office_name.upper() == 'HR' and int(number_Of_Years) <= 10):
            print (HR_Value * 5)
        else:
            print("office not found")
    else:
        print('you should Entered Alphabet Character on the OFFICE NAME and digit on the NUMBER OF YEARS')