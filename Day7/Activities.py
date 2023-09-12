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

def calculator(chosen):
    value_1 = int(input('Enter first number: '))
    value_2 = int(input('Enter second number: '))
    if int(chosen) == 1:
        out = value_1 + value_2
        return(f'output are: {out}')
    elif int(chosen) == 2:
        out = value_1 - value_2
        return(f'output are: {out}')
    elif int(chosen) == 3:
        out = value_1 * value_2
        return(f'output are: {out}')
    elif int(chosen) == 4:
        out = value_1 / value_2
        return(f'output are: {out}')

def Activity2():
    try:
        while True:
            chosen = input('Enter number 1-4\nno.1 for Addition\nno.2 for Subtration\nno.3 for Multiply\nno.4 for Division\nno 0 for exit: ')
            if int(chosen) != 0:
                print(calculator(chosen))
            else:
                break
    except ZeroDivisionError:
        print('Division By Zero is Error !!')
    except :
        print('Invalid input, Please Enter Numbers only')

Activity2()