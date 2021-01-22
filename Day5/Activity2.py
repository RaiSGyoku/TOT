
def reverseWord(inp):
    backwards = inp[::-1]
    return(f'original word: {inp} produced: {backwards} number of character: {len(inp)}')

print(reverseWord( inp = input('Enter word here: ')))