class Compound_Conditions_using_and_or_function():
    def using_and_function(a,b,c):
        if a > b and c > a: # and sample
            print ('Both Conditions are True')
        else:
            print ('one Conditions is False')

    def using_or_function(a,b,c):
        if a > b or c < a: # or sample
            print ('one Conditions is True')
        else:
            print ('All Conditions are False')

class built_in_methods():
    def isupper_sample(sample_text):
        print(sample_text.isupper()) #checking if the str1 is a upper case characters

    def islower_sample(sample_text):
        print(sample_text.islower()) #checking if the str2 is a lower case characters

    def isdigit_sample(sample_text):
        print(sample_text.isdigit()) #checking if the str1 is a digit case characters

    def isalpha_sample(sample_text):
        print(sample_text.isalpha()) #checking if the str2 is a alphabet case characters

    def bool_with_built_in(sample_text1,sample_text2):
        if sample_text1.isupper() == True and sample_text2.islower() == True:
            print("string 1 is in all upper case and string 2 is in all lower case")
    
a = 200
b = 33
c = 500

Compound_Conditions_using_and_or_function.using_and_function(a,b,c)
Compound_Conditions_using_and_or_function.using_or_function(a,b,c)

str1 = "MARK HAMBER"
str2 = "python"
built_in_methods.isupper_sample(str1)
built_in_methods.islower_sample(str2)
built_in_methods.isdigit_sample(str1)
built_in_methods.isalpha_sample(str2)
built_in_methods.bool_with_built_in(str1,str2)
