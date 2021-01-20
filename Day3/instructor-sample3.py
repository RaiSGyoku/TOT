#built-in methods

str1 = "MARK HAMBER"
str2 = "python"

print(str1.isupper()) #checking if the str1 is a upper case characters
print(str2.islower()) #checking if the str2 is a lower case characters
print(str1.isdigit()) #checking if the str1 is a digit case characters
print(str2.isalpha()) #checking if the str2 is a alphabet case characters

if str1.isupper() == True and str2.islower() == True:
    print("string 1 is in all upper case and string 2 is in all lower case")
