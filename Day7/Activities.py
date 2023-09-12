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
    
Activity1() # ['jasper Santos Santos', 'Naruto jimenez mori', 'julien umali jesusa', 'jasper lee Dela Cruz']