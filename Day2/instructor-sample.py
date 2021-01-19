# Strings and String PLace Holder

name = "Jasper"
food = 'Tocino'
game = 'Egmaes'
a = 10                  #integer value

mgs = "Number is {}"    #setting message output
disp = mgs.format(a)    #formating the message

print(disp)             #displaying output

sampleText1 = "My name is {} i love {} and playing {}"
sampleText1a = sampleText1.format(name, food, game)

print(sampleText1a)


sampleText2 = "My name is {2} i love {1} and playing {0}" # playing with index
sampleText2a = sampleText2.format(game, food, name)       # playing with index

print(sampleText2a)


sampleText3 = "My name is {newName} i love {newFood} and playing {newGame}" # use the new variable name on the place holder to indicate the index
sampleText3a = sampleText3.format( newName = 'mark', newFood = 'sandwich', newGame = 'ML')  # new declare variables

print(sampleText3a)


sampleText4 = "My name is {} i love {} and playing {}" # 
sampleText4a = sampleText4.format("mark", 'hotdog', 'ml') 
print(sampleText4a)


inputvariable = input("enter here")     # using input function

msg = "Message is {}"                   # setting message output
disp = msg.format(inputvariable)        # formating message output
print(disp)                             # displaying output