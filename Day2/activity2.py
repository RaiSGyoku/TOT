name =  input('Enter Employee Name: ')
hours = input('Enter Number of Hours: ')
sss_contrib = input('SSS contribution: ')
phil_health = input('Phil Health: ')
housing_loan =  input('Housing Loan: ')

ratePerHour = 500
gross = ratePerHour * int(hours)
total_deduc = (int(sss_contrib) + int(phil_health) + int(housing_loan))
taxed = gross * 0.12
netIncome = gross -( int(total_deduc) + taxed) 

newTotal_deduc = ( int(total_deduc) + taxed) 

print('==========PAYSLIP==========')
print("==========EMPLOYEE INFORMATION==========")
print (f'Employee name: {name.upper()} \nRendered Hours: {hours} \nRate Per Hour: {ratePerHour} \nGross Salary: {float(gross)} ')
print("==========DEDUCTION==========")
print(f'SSS: {sss_contrib} \nPhilHealth: {phil_health} \nHousing Loan: {housing_loan} \nTAX: {taxed} \nTotal Deduction: {newTotal_deduc} \n\nNet Salary: PHP {netIncome}')
