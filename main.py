from Day1.instructor_samples import *# Casting_and_Operand,Variable_Data_Type_sample,Input_Functions


def main():
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

if __name__ == "__main__":
    main()