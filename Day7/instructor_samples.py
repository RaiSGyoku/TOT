class random_fucntion():
    import random
    
    def using_randint_fucntion(generated_random = random):
        print(generated_random.randint(75,90))

    def using_randint_function_with_for_loop(generated_random = random):
        for i in range(5):
            print(generated_random.randint(1,10))

    def using_choice_for_int(generated_random = random):
        print(generated_random.choice([10,20,30,40,50]))
