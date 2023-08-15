from Day2.instructor_samples import *
from Day1.instructor_samples import *# Casting_and_Operand,Variable_Data_Type_sample,Input_Functions


def Day1():
    print('this are the sample of variable and Data Types: ')
    print('Integer Sample: ',Variable_Data_Type_sample.integer_sample())
    print('String Sample: ',Variable_Data_Type_sample.string_sample())
    print('Float Sample: ',Variable_Data_Type_sample.float_sample())
    print('Boolen Sample: ',Variable_Data_Type_sample.bool_sample())
    
    print('this are the sample of casting and operand: ')
    print('sum: ',Casting_and_Operand.sum('10','10','1.8'))
    print('diff: ',Casting_and_Operand.diff('10','10'))
    print('prod: ',Casting_and_Operand.prod('10','10'))
    print('qou: ',Casting_and_Operand.qou('10','10'))

    print('Here is the sample for input function')
    Input_Functions.Input_Sample()

def Day2():
    name = "Jasper"
    food = 'Tocino'
    game = 'Egmaes'
    a = 10                  #integer value

    Sample_Text1 = "JASPER MARK"
    Sample_Text2 = 'mark'

    print(Format_String_Functions.length_Sample(Sample_Text1))
    print(Strings_and_PLace_Holders.Input_and_Place_Holder())

def main():

    Day2()
    

if __name__ == "__main__":
    main()