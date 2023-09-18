def read_File():
    #file = open("Day9/file.txt","r")
    file = open("Day9/info.txt","r")
    print (file.read())
    file.close()

def write_File():
    file = open("Day9/info.txt", "a")
    file.write("New Text")
    file.close()

    file = open("Day9/info.txt", "r")
    print(file.read())

def remove_file():
    import os
    
    os.remove("Day9/info.txt")