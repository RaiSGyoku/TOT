class random_fucntion():
    import random
    
    def using_randint_fucntion(generated_random = random):
        print(generated_random.randint(75,90))

    def using_randint_function_with_for_loop(generated_random = random):
        for i in range(5):
            print(generated_random.randint(1,10))

    def using_choice_for_int(generated_random = random):
        print(generated_random.choice([10,20,30,40,50]))

    def using_choice_for_str(generated_random = random):
        print(generated_random.choice(['yes','no','maybe','nope']))
    
    def using_choice_with_dictionary(generated_random = random):
        names = ['Nobita','Naruto','Picolo','Asta','Santos','julien','jan','mark','jasper','calliope']
        print(generated_random.choice(names))

class Handling_Exceptions():
    def sample_1():
        try:
            result = 100/0
        except ZeroDivisionError:
            print('Division by zero is error !!')
        except:
            print("Wrong input")
        else:
            #print("No Exceptions." , "Display the result: is: ", result)
            print("No Exceptions." , f"Display the result: is: {result}")
        finally:
            print("This will Execute no matter what")

    def sample_2():
        try:
            result = 100/a
        except ZeroDivisionError:
            print('Division by zero is error !!')
        except:
            print("Wrong input")
        else:
            #print("No Exceptions." , "Display the result: is: ", result)
            print("No Exceptions." , f"Display the result: is: {result}")
        finally:
            print("This will Execute no matter what")