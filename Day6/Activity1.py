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
    

    



