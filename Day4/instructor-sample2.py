#Iteration looping (For loop using range method)

for a in range(10,20):
    print(a)


fruits = ["mango","banana","apple"]

for index in range(len(fruits)):
    if index == 2:
        print (fruits[index] )
    print("Current fruit:", fruits[index] )
    #print(fruits[index] )
    print(index)
