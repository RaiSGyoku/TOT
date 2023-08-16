# Variable and Data Type

class Variable_Data_Type_sample():
    def integer_sample():
        a = 5           # a is  a variable under the integer Date Type 
        return(a)

    def string_sample():    
        b = "john"      # b is  a variable under the String Date Type 
        return(b)

    def float_sample():
        c = 1.25        # c is  a variable under the float Date Type 
        return(c)

    def bool_sample():    
        d = True        # d is a variable under the boolen Date Type 
        return(d)
# "" and '' are the same for the Data Type

#casting and operant
class Casting_and_Operand():

    def sum(x,y,z):
        return (int(x) + int(y) + float(z))
    
    def diff(x,y):
        return( int(x) - int(y) )
    
    def prod(x,y):
        return( int(x) * int(y) )
    
    def qou(x,y):
        return(int(x) / int(y)) 

# inpu() function
class Input_Functions():
    def Input_Sample():
        name = input('Enter Full Name: ')
        email = input('Enter Email: ')

        return(''
            f'Name: {name} \n'
            f'Email: {email}'
        '')        
    
class basic_sample():
    def Hello_World():
        return('Hello World')