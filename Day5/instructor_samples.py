#Defining and Calling a Function
class Defining_and_Calling_a_Function():
    def greet():
        print('hi')


class Function_with_Parameters():
    def greet(name):
        print("hi " + name)

class Function_with_default_value_parameter():
    def greet(name = 'John Doe'):
        print('hi '+ name)




Defining_and_Calling_a_Function.greet() #greet() 
Function_with_Parameters.greet('john')
Function_with_default_value_parameter.greet()
Function_with_default_value_parameter.greet('anna')