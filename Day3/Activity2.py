offi_name0 = input('Enter Office Name: ')
numbOfYears = input('Enter Number of Years: ')

itValue = 1000
accValue = 1200
hrValue = 1500

#print (itValue * 10)
#print (accValue * 5)
if (offi_name0.isalpha() == True and numbOfYears.isdigit() == True):
    if (offi_name0.upper() == 'IT' and int(numbOfYears) >= 10):
        print (itValue * 10)
    elif (offi_name0.upper() == 'IT' and int(numbOfYears) <= 10):
        print (itValue * 5)
        #
    elif (offi_name0.upper() == 'ACCT' and int(numbOfYears) >= 10):
        print (accValue * 10)
    elif (offi_name0.upper() == 'ACCT' and int(numbOfYears) <= 10):
        print (accValue * 5)    
        #
    elif (offi_name0.upper() == 'HR' and int(numbOfYears) >= 10):
        print (hrValue * 10)    
    elif (offi_name0.upper() == 'HR' and int(numbOfYears) <= 10):
        print (hrValue * 5)
    else:
        print("office not found")
else:
    print('you should Entered Alphabet Character on the OFFICE NAME and digit on the NUMBER OF YEARS')


