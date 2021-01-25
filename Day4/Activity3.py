
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
        print(f'lsit of Words {wordbank}')
        print("Thank you")
        break