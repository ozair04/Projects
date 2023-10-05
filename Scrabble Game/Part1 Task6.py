alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def onlyEnglishLetters(word):
    for letter in word:
        if letter.upper() not in alphabet:
            result = False
            break
        else:
            result = True
    return result
dictionary = open("dictionary.txt").read().split('\n')
tiles = open("tiles.txt").read().split('\n')
def canBeMade(word, myTiles):
    for letter in word:
        if letter.upper() not in myTiles:
            return False
            break
        else:
            myTiles.remove(letter.upper())
    return True
#function isValid defined to validate if a word is viable and can be made from a given list of tiles and is also in the dictionary
def isValid(word, myTiles, dictionary):
    if onlyEnglishLetters(word) == True:
        if word.upper() in dictionary:
            if canBeMade(word, myTiles) == True:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
print(isValid("hello", ['H', 'S', 'E', 'L', 'O', 'A', 'L'], dictionary))


