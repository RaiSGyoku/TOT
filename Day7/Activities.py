def Activity1():
    import random

    first_name = ['Nobita','Naruto','Picolo','Asta','Santos','julien','jan','mark','jasper','calliope']
    middle_name = ['Apolonio','Santos','Cortez','peneda','bautista','Teodosio','umali','buhay','lee','jimenez']
    last_name = ['Santos','Dela Cruz','Vina','peneda','cruz','cortez','De jesus','jesusa','tura','mori']

    new_list = []

    while True:
        inp1 = input('want to generate new name press y if yes: ')
        if (inp1.upper() == 'Y'):
            ind_fname = random.randint(0, 9)
            ind_Mname = random.randint(0, 9)
            ind_lname = random.randint(0, 9)

            new_list.append(first_name[ind_fname] +' '+ middle_name[ind_Mname] +' '+ last_name[ind_lname])
            continue
        else:
            print('thank you')
            print(new_list)
            break
    
# ['jasper Santos Santos', 'Naruto jimenez mori', 'julien umali jesusa', 'jasper lee Dela Cruz']

def contidtion_Test(inpChoose):
    if int(inpChoose) == 0:
        return(False)
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

def Activity2():
    try:
        inpChoose = input('Enter number 1-4\nno.1 for Addition\nno.2 for Subtration\nno.3 for Multiply\nno.4 for Division\nno 0 for exit: ')
        while contidtion_Test(inpChoose) is True:
           
            contidtion_Test(inpChoose)

    except ZeroDivisionError:
        print('Division By Zero is Error !!')
    #except :
    #    print('Invalid input, Please Enter Numbers only')

Activity2() 