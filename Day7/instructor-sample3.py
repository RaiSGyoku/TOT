# Handling Exceptions sample 2

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