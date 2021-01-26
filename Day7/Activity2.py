try:
    while True:
        inpChoose = input('Enter number 1-4\nno.1 for Addition\nno.2 for Subtration\nno.3 for Multiply\nno.4 for Division\nno 0 for exit: ')
        if int(inpChoose) == 0:
            break
        else:
            inpVal1 = int(input('Enter first number: '))
            inpVal2 = int(input('Enter second number: '))
            if int(inpChoose) == 1:
                out = inpVal1 + inpVal2
                print(f'output are: {out}')
            elif int(inpChoose) == 2:
                out = inpVal1 - inpVal2
                print(f'output are: {out}')
            elif int(inpChoose) == 3:
                out = inpVal1 * inpVal2
                print(f'output are: {out}')
            elif int(inpChoose) == 4:
                out = inpVal1 / inpVal2
                print(f'output are: {out}')
except ZeroDivisionError:
    print('Division By Zero is Error !!')
except :
    print('Invalid input, Please Enter Numbers only')


#finally:
