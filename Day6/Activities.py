def Activity1():
    dict = {}
    while True:
        inp1 = int(input('press 1: to add\npress 2: to delete\npress 3: to end '))
        if (inp1 == 1):
            inpKey = input('Enter Key: ')
            inpValue = input('Enter Value: ')
            dict[inpKey] = inpValue
            print(dict)
        elif (inp1 == 2):
            inpKey = input('Enter Key: ')
            del dict[inpKey] 
            print(dict)
        elif (inp1 == 3):
            print('THANK YOU')
            break

        inResp = input('wants to try again?, Press y if Yes if no press anykey: ')
        if (inResp.upper() == 'Y'):
            continue
        else:
            print('thank you')
            break
    
class Activity2():
    
    
    def SalaryDeduction(loan,Insurance,totalGross):
        tax = 0.12
        taxed = int(totalGross) * tax
        return (int(loan)+int(Insurance)+taxed)
    
    def grossSalary(hours):
        ratePerHour = 500 
        return (ratePerHour * int(hours))
    
    # will be responsible for computing the net salary.
    def NetSalary(totalGross, totalDeduction):
        return (totalGross - totalDeduction )
    #Tax(12% of the gross salary)
    
    def payroll():
        inpName = input('Enter Name: ')
        inpHour = input('Enter Hour: ')
        inpLoan = input('Enter Loan: ')
        inpHealth_Insurance =  input('Enter Health Insurance: ')
        
        print ('the gross is: ',Activity2.grossSalary(int(inpHour)))
        print ('the Deduction is: ',Activity2.SalaryDeduction(int(inpLoan),int(inpHealth_Insurance),Activity2.grossSalary(int(inpHour)) ) )
        print ('the NetIncome is: ',Activity2.NetSalary(Activity2.grossSalary(int(inpHour)),Activity2.SalaryDeduction(int(inpLoan),int(inpHealth_Insurance),Activity2.grossSalary(int(inpHour)) )))


Activity2.payroll()