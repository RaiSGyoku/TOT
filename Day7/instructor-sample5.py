try:
    file = open("sample6.txt")
except FileNotFoundError as fileError:
    print(fileError)
else:
    print("file is Found!")