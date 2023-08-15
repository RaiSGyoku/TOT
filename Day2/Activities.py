def Activity1():
    input_Noun_1 = input('Enter noun 1: ') #advice
    input_Noun_2 = input('Enter noun 2: ') #fear
    input_Noun_3 = input('Enter noun 3: ') #hope
    input_Adjective_1 = input('Enter adjective 1: ') #claim
    input_Adjective_2 = input('Enter adjective 2: ') #faithful
    input_Adjective_3 = input('Enter adjective 3: ') #delightful

    lyrics = '\n\n\n original: Well, if you wanted honesty Thats all you had to say I never want to let you down Or have you go, its better off this way For all the dirty looks The photographs your boyfriend took Remember when you broke your foot From jumping out the second floor? \n\n\n'

    new_Lyrics = f' Replaced: {input_Adjective_3.upper()} Well, if you wanted {input_Noun_1.upper()} Thats all you had to say I never {input_Noun_2.upper()} to let you down Or have you go, its {input_Noun_3.upper()} off this way For all the dirty looks The photographs your boyfriend {input_Adjective_1.upper()} Remember when you broke your foot From jumping out the second floor {input_Adjective_2.upper()}?'

    return(''
        f'{lyrics}'
        f'{new_Lyrics}'
    '')

def Activity2():
    name =  input('Enter Employee Name: ')
    hours = input('Enter Number of Hours: ')
    sss_contrib = input('SSS contribution: ')
    phil_health = input('Phil Health: ')
    housing_loan =  input('Housing Loan: ')

    rate_Per_Hour = 500
    gross = rate_Per_Hour * int(hours)
    total_deduc = (int(sss_contrib) + int(phil_health) + int(housing_loan))
    taxed = gross * 0.12
    netIncome = gross -( int(total_deduc) + taxed) 

    new_Total_deduc = ( int(total_deduc) + taxed) 
    return(''
        '\n==========PAYSLIP==========\n'
        "==========EMPLOYEE INFORMATION==========\n"
        f'Employee name: {name.upper()} \nRendered Hours: {hours} \nRate Per Hour: {rate_Per_Hour} \nGross Salary: {float(gross)} \n'
        "==========DEDUCTION==========\n"
        f'SSS: {sss_contrib} \nPhilHealth: {phil_health} \nHousing Loan: {housing_loan} \nTAX: {taxed} \nTotal Deduction: {new_Total_deduc} \n\nNet Salary: PHP {netIncome}'
    '')