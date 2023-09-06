#Defining and Calling a Function
class Defining_and_Calling_a_Function():
    def greet():
        print('hi')


class Function_with_Parameter():
    def greet(name):
        print("hi " + name)

class Function_with_default_value_parameter():
    def greet(name = 'John Doe'):
        print('hi '+ name)

class Function_with_return():
    def greet():
        return('hi ')

class Function_with_Parameters():
    def solve(num1, num2):
        sum = (num1+num2)
        return (f'sum is {sum}')




Defining_and_Calling_a_Function.greet() #greet() 
Function_with_Parameter.greet('john')
Function_with_default_value_parameter.greet()
Function_with_default_value_parameter.greet('anna')
print(Function_with_return.greet())
print(Function_with_Parameters.solve(2,3))