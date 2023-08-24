#Iteration_looping

# Iteration looping (While loop)
def While_loop_sample(a = 1): #declared
    while a < 6: #condition
        #b=input('Enter') test
        print(a)
        a += 1 #  a = a + 1
        
        if a == 2:
            print(a)
            a = 10 #loop terminator 
        else :
            print ('9')

# Iteration looping (For loop using in)
def For_Loop_with_In_sample():
    names = ["Mike","Ana","Jun"]
    listval = [1,2,3,"ggg"]
    for name in names:
        print(name)
        #if name == "Mike":
        #    print (f'{name} is good')

# Iteration looping (For loop using range method)
def For_Loop_with_Range_sample():
    for a in range(10,20):
        print(a)
        
    fruits = ["mango","banana","apple"]

    for index in range(len(fruits)):
        if index == 2:
            print (fruits[index] )
        print("Current fruit:", fruits[index] )
        #print(fruits[index] )
        print(index)

# Iteration looping (For loop using having break function)
def For_Loop_with_Break_sample():
    for letter in "python":
        if letter == 't':
            break
        print("Current Letter", letter)

# Iteration looping (For loop using continue function )
def For_Loop_with_Continue_sample():
    for letter in "python python":
        if letter == 't' or letter == 'h':
            continue
        print("Current Letter", letter)

# Iteration looping (For loop using having pass function )
def For_Loop_with_Pass_sample():
    for letter in "python":
        if letter == 'h' :
            pass # pass is a place holder for the to be added feature
            print('this is the pass block')
        print("Current Letter", letter)
    print('goodbye')

def List_String_sample():
    foods = ["cake", "burger", "fries"]
    print(foods[1]) # print burger

def List_Number_sample():
    numbers = [1, 2, 3, 4, 5]
    print(numbers[3]) # print 1

def List_Number_use_Variable_for_Index_value():
    numbers = [1, 2, 3, 4, 5]
    a =2
    print(numbers[a]) # use variable int value for the index value

# changing value in list
def Change_Value_in_List():
    male = ["JOHN", "Mike"]
    print(male[0])

    male[0] = 'Frank'
    print(male[0])

# append and insert method for list
def List_Append_sample():
    numlist = [1,2,3,4,5]
    numlist2 = [6,7,8,9,10]

    numlist.append(6)
    numlist.append(numlist2[0]) #sample personal
    print(numlist)

def List_Insert_sample():
    male =['Jasper','Peter','Packer']
    male.insert(1,'Mark')
    print(male)

# remove and pop method for list
def List_Remove_sample():
    male =['Jasper','Peter','Packer']
    male.remove('Packer')#the text is the removed

def List_Pop_sample():
    male =['Jasper','Peter','Packer']
    male.pop(1) #the index is the removed
    print(male)

# sort and reverse method for list
def List_Sort_Int_sample():
    numlist = [5,4,2,3,1]
    numlist.sort(reverse=True) #sort as highest to lowest same as reverse
    numlist.sort() #sort as numeric
    print(f'sort: {numlist}')

def List_Sort_Str_sample():
    pets = ['dog', 'cat']
    pets.sort() #sort as aplhebet
    print(f'sort: {pets}') 

def List_Reverse_int_sample():
    numlist2 = [1,2,3,4,5]
    numlist2.reverse()#sort as numeric
    print(numlist2)

def List_Reverse_Str_sample():
    pets2 = ['dog', 'cat']
    pets2.reverse() #sort as aplhebet
    print(pets2) 

# count and index method for list
def List_Count_sample():
    numlist = [25,44,22,13,25]
    counter = numlist.count(25)
    print(counter)

def List_Index_sample():
    numlist2 = [25,44,22,13,25]
    indexPos = numlist2.index(13)
    print(indexPos)