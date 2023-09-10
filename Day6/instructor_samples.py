class Tuple():
    def usng_len_Function():
        MyAnime = ('Naruto', 'Babidi', 'Doreamon','conan')
        print(len(MyAnime)) #count the item inside of the tuple

    def usng_max_Function():
        myGrade = (89,90,92,89,87)
        print(max(myGrade)) #getting the highest value in the tuple

    def basic_sample():
        tup1 = ('physical','chemistry',1997,2000)
        tup2 = (1,2,3,4,5,6,7)
        
        print("tup1[0]:", tup1[0])
        print("tup2[1:5]:", tup2[1:5]) # name of tuple[index:range] 
        
        print(f"tup2[1:len(tup2): {tup2[1:len(tup2)]}") #can be use as well 

    def tuple_to_list_convertion():
        thisList = [123, 'xyz', 'zara', 'abc']
        thisTuple = tuple(thisList)

        print(f'Tuple Items: {thisTuple}')

    def using_delete_function():
        MyAnime = ('Naruto', 'Goku', 'Zoneo')
        del MyAnime
        print(MyAnime) # this will raise an error because the tuple is no longer exists

    def merging_two_tuple():
        #concatenating tuple sample
        
        team7 = ('Naruto','Sasuke','Sakura')
        teamBa = ('Zoneo','Damulag','Babidi')

        teamAnime = (team7+teamBa)
        print(teamAnime)


        newteamAnime=sorted(teamAnime) # using short method
        print(newteamAnime)

    def check_value_in_tuple():
        team7 = ('Naruto','Sakura','Sasuke')
        if 'Naruto' in team7:
            print('yes, "Naruto" is in the Team7 tuple ')


class Dictionary():
    def baic_sample():
        dict = {'Name': 'Cyrel', 'Age': 19, 'Class':'1st'}
        
        print('dict["Name"]:' ,dict['Name'])
        print('dict["Age"]:' ,dict['Age'])
        print('dict["Class"]:' ,dict['Class'])
        #print(f"dict['Class']: {dict['Class']}" ) #can be use the format
        print(dict)

    def update_Dictionary_value():
        dict = {'Name': 'Cyrel', 'Age': 19, 'Class':'1st'}
        dict['Age'] = 23 #update existing entry
        dict['School'] = 'Gallanosa NHS' #update existing entry

        print('dict["Age"]:' ,dict['Age'])
        print('dict["School"]:' ,dict['School'])
        #print(f"dict['Class']: {dict['Class']}" ) #can be use the format

    def using_del_function():
        dict = {'Name': 'Cyrel', 'Age': 19, 'Class':'1st'}
        del dict['Name']    #remove entry
        
    def using_clear_function():
        dict = {'Name': 'Cyrel', 'Age': 19, 'Class':'1st'}
        dict.clear()        #remove all entries in dict
        #del dict            #delete entire dictionary

class sets():
    def basic_sample():
        fruits={'apple','banana','cherry'}
        print(fruits)

    def using_add_function():
        fruits={'Apple','Banana','santol'}
        fruits.add('Guyabano')
        print(fruits)

    def using_update_function():
        progs = {'C','C#','Java'}
        progs.update(['PHP','JS'])
        print(progs)

class modules_sample():
    def add(num1, num2):
        return(int(num1)+int(num2))
    
    def subtraction(num1, num2):
        return(int(num1)-int(num2))

    def model():
        num1 = int(input("Enter 1st number: "))
        num2 = int(input("Enter 2nd number: "))
        
        print ('the sum is: ',modules_sample.add(num1,num2))
        print ('the subtraction is: ',modules_sample.subtraction(num1,num2))

Tuple.usng_len_Function()
Tuple.usng_max_Function()

Dictionary.baic_sample()
Dictionary.update_Dictionary_value()

modules_sample.model()