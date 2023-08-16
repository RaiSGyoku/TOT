class Strings_and_PLace_Holders():

    def Place_Holder_sample1(a):
        mgs = "Number is {}"    #setting message output
        disp = mgs.format(a)    #formating the message

        return(disp)             #displaying output
    
    def Place_Holder_Sample2(name,food,game):
        sample_Text = "My name is {} i love {} and playing {}"
        disp = disp.format(name, food, game)
        return(disp)
    
    def Place_Holder_Sample3(name,food,game):
        sample_Text = "My name is {2} i love {1} and playing {0}" # playing with index
        disp = disp.format(game, food, name)       # playing with index
        return(disp)

    def Place_Holder_Sample4(name,food, game):
        sample_Text = "My name is {newName} i love {newFood} and playing {newGame}" # use the new variable name on the place holder to indicate the index
        disp = sample_Text.format( newName = 'mark', newFood = 'sandwich', newGame = 'ML')  # new declare variables
        return(disp)

    def Place_Holder_Sample5(name,food,game):
        sample_Text = "My name is {} i love {} and playing {}" # trying simple string only
        disp = disp.format("mark", 'hotdog', 'ml') # trying simple string only
        return(disp)
    
    def Input_and_Place_Holder():
        input_variable = input("Enter Message here: ")     # using input function

        msg = "Message is {}"                   # setting message output
        disp = msg.format(input_variable)        # formating message output
        return(disp)                             # displaying output
    
    # Strings and String PLace Holder using %

    def Numbers_String_Format1():
        item = 'key'
        cost = 100.00
        quantity = 5

        format_disp = "Product: %s cost: %.2f quantity: %i" %(item, cost, quantity)
        return(format_disp)

    # Strings and String PLace Holder using F or f
    def Numbers_String_Format2():
        item = 'key'
        cost = 100.00
        quantity = 5

        format_disp = f"The product {item} cost {cost * quantity : .2f}  pesos" # useful for printing or displaying info Specially with computation
        return(format_disp)
    
class Format_String_Functions():
    
    def Upper_Sample1():
        sample_Text = 'test'
        return(sample_Text.upper())

    def Lower_sample1():
        sample_Text = 'TEST'
        return(sample_Text.lower())
    
    def Upper_Sample2(Sample_Text2):
        sample_Text = 'test'
        return("Name in all upper "+ Sample_Text2.upper())

    def Lower_sample2(Sample_Text1):
        return("Name in all lower "+ Sample_Text1.lower())

    def Capitalize_Sample(Sample_Text1):
        return("Name in all capitalize "+ Sample_Text1.capitalize())
    
    def Title(Sample_Text1):
        return("Name in all title "+ Sample_Text1.title())
    
    def Replace_sample(Sample_Text1,Sample_Text2):

        new_Name = Sample_Text1.replace("JASPER", Sample_Text2.upper())
        return(new_Name)
    
    def Split_Sample(Sample_Text1):
        splited_Name = Sample_Text1.split(" ") #split
        return(splited_Name)

    def Split_via_index(splited_Name):

        format_disp1 = f'Name 1st word:' +str(splited_Name[0])
        format_disp2 = f'Name 2st word:' +str(splited_Name[1])
        result =  format_disp1 +'\n' + format_disp2
        return(result)
    
    def length_Sample(Sample_Text):
        #disp_result = "length of name", len(Sample_Text1) # not working good on return function
        disp_result = f"length of name {len(Sample_Text)}"
        return(disp_result)
    
import math
class Numeric_Functions():

    def Round_Sample(grade):
        return(round(grade,1))
    
    def Math_Ceiling_Sample(grade1,grade2):
        return(''
            f'{math.ceil(grade1)}\n'
            f'{math.ceil(grade2)}'
        '')
    
    def Math_Floor_Sample(grade1,grade2):
        return(''
            f'{math.floor(grade1)}\n'
            f'{math.floor(grade2)}'
        '')

    def exponent_sample1():
        return(pow(2,3))
    
    def exponent_sample2():
        return(2**3) # same as Pow()