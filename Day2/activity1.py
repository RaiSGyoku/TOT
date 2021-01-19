inputn1 = input('Enter noun 1 ') #advice
inputn2 = input('Enter noun 2 ') #fear
inputn3 = input('Enter noun 3 ') #hope
inputa1 = input('Enter adjective 1 ') #claim
inputa2 = input('Enter adjective 2 ') #faithful
inputa3 = input('Enter adjective 3 ') #delightful

lyrics = '\n\n\n original: Well, if you wanted honesty Thats all you had to say I never want to let you down Or have you go, its better off this way For all the dirty looks The photographs your boyfriend took Remember when you broke your foot From jumping out the second floor? \n\n\n'

newLyrics = f' Replaced: {inputa3.upper()} Well, if you wanted {inputn1.upper()} Thats all you had to say I never {inputn2.upper()} to let you down Or have you go, its {inputn3.upper()} off this way For all the dirty looks The photographs your boyfriend {inputa1.upper()} Remember when you broke your foot From jumping out the second floor {inputa2.upper()}?'

print(lyrics)
print(newLyrics)