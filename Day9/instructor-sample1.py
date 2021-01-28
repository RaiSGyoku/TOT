#write to a file

file = open("Day9/info.txt", "a")
file.write("New Text")
file.close()

file = open("Day9/info.txt", "r")
print(file.read())