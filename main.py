from Day2.instructor_samples import *
from Day1.instructor_samples import *# Casting_and_Operand,Variable_Data_Type_sample,Input_Functions


def Day1():
    print('this are the sample of variable and Data Types: ')
    print('Integer Sample: ',Variable_Data_Type_sample.integer_sample())
    print('String Sample: ',Variable_Data_Type_sample.string_sample())
    print('Float Sample: ',Variable_Data_Type_sample.float_sample())
    print('Boolen Sample: ',Variable_Data_Type_sample.bool_sample())
    
    print('\nthis are the sample of casting and operand: ')
    print('sum: ',Casting_and_Operand.sum('10','10','1.8'))
    print('diff: ',Casting_and_Operand.diff('10','10'))
    print('prod: ',Casting_and_Operand.prod('10','10'))
    print('qou: ',Casting_and_Operand.qou('10','10'))

    print('\nHere is the sample for input function')
    Input_Functions.Input_Sample()

def Day2():
    name = "Jasper"
    food = 'Tocino'
    game = 'Egmaes'
    a = 10                  #integer value

    Sample_Text1 = "JASPER MARK"
    Sample_Text2 = 'mark'

    grade1 = 95.50
    grade2 = 95.20



    print('\nthis are the sample of Strings, Place Holder and Numeric: ')
    
    #print(f"sample of Input and Place Holder\n{Strings_and_PLace_Holders.Input_and_Place_Holder()}\n")
    print(f"sample of lenght functions \n{Format_String_Functions.length_Sample(Sample_Text1)}\n")
    
    
    print("\nNumeric Sample")
    print(f"sample of round function\n{ Numeric_Functions.Round_Sample(grade1)}\n")
    print(f"sample of math ceiling function\n{Numeric_Functions.Math_Ceiling_Sample(grade1,grade2)}\n" )
    print(f"sample of math floor function\n{ Numeric_Functions.Math_Floor_Sample(grade1,grade2)}\n")
    print(f"sample of pow function\n{ Numeric_Functions.exponent_sample1()}\n")
    print(f"alternative of pow function\n{ Numeric_Functions.exponent_sample2()}\n")

def main():
    #Day1()
    Day2()
    

if __name__ == "__main__":
    main()