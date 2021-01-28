import os

try:
    while True:
        inpChoice = input("Enter no.1 for Add Record\nEnter no.2 for view Records\nEnter no.3 for clear All Records\nEnter no.4 for Exit\n Input: ")
        if int(inpChoice) == 1:
            inpName = input("Enter name: ")
            inpEmail = input("Enter Email: ")
            inpAddress = input("Enter Address: ")
    
            file = open("Day9/Activityinfo.txt", "a")
            file.write(f"Name = {inpName}, Email = {inpEmail}, Address = {inpAddress}\n")
            file.close()

        elif int(inpChoice) == 2:
            file = open("Day9/Activityinfo.txt","r")
            print (file.read())
            file.close()

        elif int(inpChoice) == 3:
            os.remove("Day9/Activityinfo.txt")
            file = open("Day9/Activityinfo.txt", "a")
            file.close()

        elif int(inpChoice) == 4:
            print("Thank You")
            break
        
        inResp = input('wants to try again?, Press y if Yes if no press anykey: ')
        if (inResp.upper() == 'Y'):
            continue
        else:
            print('thank you')
            break
except:
    print("invalid Input")