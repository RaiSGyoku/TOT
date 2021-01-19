# String formatting function

str1 = 'test'
print(str1.upper())

str2 = 'TEST'
print(str1.lower())

name = "JASPER MARK"
s = 'mark'

print ("Name in all upper "+ s.upper())
print ("Name in all lower "+ name.lower())
print ("Name in all capitalize "+ name.capitalize())
print ("Name in all title "+ name.title())

splitName = name.split(" ") #split

print (splitName)

print('Name 1st word:' +str(splitName[0]))
print('Name 1st word:' +str(splitName[1]))

newName = name.replace("JASPER", s.upper())

print(newName)



print ("length of name", len(name))