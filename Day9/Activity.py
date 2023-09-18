import os

def is_True(inResp):
    if (inResp.upper() == 'Y'):
        return True
    else:
        print('thank you')
        return False
    
def add(name,email,address):
    file = open("Day9/Activityinfo.txt", "a")
    file.write(f"Name = {name}, Email = {email}, Address = {address}\n")
    file.close()

def view():
    file = open("Day9/Activityinfo.txt","r")
    print (file.read())
    file.close()

def delete():
    os.remove("Day9/Activityinfo.txt")
    file = open("Day9/Activityinfo.txt", "a")
    file.close()
    
class Activity():
    try:
        inResp = 'y'
        while is_True(inResp):
            chosen = input("Enter no.1 for Add Record\nEnter no.2 for view Records\nEnter no.3 for clear All Records\nEnter no.4 for Exit\n Input: ")
            if int(chosen) == 1:
                inpName = input("Enter name: ")
                inpEmail = input("Enter Email: ")
                inpAddress = input("Enter Address: ")

                add(inpName,inpEmail,inpAddress)
                print('Added')
            
            elif int(chosen) == 2:
                view()

            elif int(chosen) == 3:
                delete()

            elif int(chosen) == 4:
                print("Thank You")
                break
            
            inResp = input('wants to try again?, Press y if Yes if no press anykey: ')
    

    except:
        print("invalid Input")

Activity()