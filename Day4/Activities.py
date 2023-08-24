def Activity1(a = 1):
    while a <= 20: #condition
        print(f'{a} Love Pyhton')
        a += 1 #  a = a + 1

def Activity2():
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

def Activity3():
    wordbank = []
    while True:
        inp= input("Enter a Word: ")

        wordbank.append(inp)
        inResp = input('wants to try again?, Press y if Yes if no press anykey: ')
        
        if (inResp.upper() == 'Y'):
            continue
        else:
            numberOfWord = len(wordbank)
            print(f'Number of Words {numberOfWord}')
            print(f'list of Words {wordbank}')
            print("Thank you")
            break