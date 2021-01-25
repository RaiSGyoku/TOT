#he user will input the following (Name,
#Hour, Loan, Health Insurance).
#8. Save your file as lastname_firstname_day6_act2.py

from Activity2_GrossSalary import grossSalary
from Activity2_SalaryDeductions import SalaryDeduction
from Activity2_NetSalary import NetSalary

inpName = input('Enter Name: ')
inpHour = input('Enter Hour: ')
inpLoan = input('Enter Loan: ')
inpHealth_Insurance =  input('Enter Health Insurance: ')

print ('the gross is: ',grossSalary(int(inpHour)))
print ('the Deduction is: ',SalaryDeduction(int(inpLoan),int(inpHealth_Insurance),grossSalary(int(inpHour)) ) )
print ('the NetIncome is: ',NetSalary(grossSalary(int(inpHour)),SalaryDeduction(int(inpLoan),int(inpHealth_Insurance),grossSalary(int(inpHour)) )))