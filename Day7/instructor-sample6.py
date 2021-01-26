try:
    file = open("Day7/sample6.txt")
except FileNotFoundError as fileError:
    print(fileError)
else:
    print("file is Found!")
finally:
    file.close()