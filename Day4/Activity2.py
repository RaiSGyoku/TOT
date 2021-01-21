in1 = int(input('Enter Value 1: '))
in2 = int(input('Enter Value 2: '))

sum = (in1 + in2)
print(sum)

a = 1 
while a < 6:
    inResp = input('wants to try again?, Press y if Yes if no press anykey: ')
    if (inResp.upper() == 'Y'):
        in1 = int(input('Enter Value 1: '))
        in2 = int(input('Enter Value 2: '))
        sum = (in1 + in2)
        print(sum)
    else:
        a = 10
        print("Thank you")
