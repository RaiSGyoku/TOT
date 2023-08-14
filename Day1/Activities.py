def Activity1():
    Name = input('Enter Full Name: ')
    MathGrade = input('Enter Math Grade: ')
    ScienceGrade = input('Enter Science Grade: ')
    EnglishGrade = input('Enter English Grade: ')

    Average = (float(MathGrade) + float(ScienceGrade) + float(EnglishGrade)) / 3

    if Average >= 4:
        return(F'Name: {Name} \n'
           F'Math Grade: {MathGrade} \n'
           F'Science Grade: {ScienceGrade} \n'
           F'EnglishGrade: {Average} \n'
           F'Average: {ScienceGrade} \n'
           F'Status: Faield'
        '')
        
    elif Average <= 3:
        return( 'Result are....\n'
           F'Name: {Name} \n'
           F'Math Grade: {MathGrade} \n'
           F'Science Grade: {ScienceGrade} \n'
           F'EnglishGrade: {Average} \n'
           F'Average: {ScienceGrade} \n'
           F'Status: Passed'
        '')

def Activity2():
    Name = 'Mark Jasper'
    MathGrade = 90.5
    ScienceGrade = 80.5
    EnglishGrade = 75
    Status = 'pass'

    return(F'Name: {Name} \n'
           F'Math Grade: {MathGrade} \n'
           F'Science Grade: {ScienceGrade} \n'
           F'EnglishGrade: {EnglishGrade} \n'
           F'Status: {Status}'
        '')