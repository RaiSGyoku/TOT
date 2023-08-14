def Activity1():
    Name = input('Enter Full Name: ')
    Math_Grade = input('Enter Math Grade: ')
    Science_Grade = input('Enter Science Grade: ')
    English_Grade = input('Enter English Grade: ')

    Average = (float(Math_Grade) + float(Science_Grade) + float(English_Grade)) / 3

    if Average >= 4:
        return(
            'Printing Result....\n'
            F'Name: {Name} \n'
            F'Math Grade: {Math_Grade} \n'
            F'Science Grade: {Science_Grade} \n'
            F'EnglishGrade: {Average} \n'
            F'Average: {Science_Grade} \n'
            F'Status: Faield'
        '')
        
    elif Average <= 3:
        return(
           'Printing Result....\n'
           F'Name: {Name} \n'
           F'Math Grade: {Math_Grade} \n'
           F'Science Grade: {Science_Grade} \n'
           F'EnglishGrade: {Average} \n'
           F'Average: {Science_Grade} \n'
           F'Status: Passed'
        '')

def Activity2():
    Name = 'Mark Jasper'
    Math_Grade = 90.5
    Science_Grade = 80.5
    English_Grade = 75
    Status = 'pass'

    return(
        F'Name: {Name} \n'
        F'Math Grade: {Math_Grade} \n'
        F'Science Grade: {Science_Grade} \n'
        F'EnglishGrade: {English_Grade} \n'
        F'Status: {Status}'
    '')

print(Activity1())
