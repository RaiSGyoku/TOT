# Handling Exceptions sample 1

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