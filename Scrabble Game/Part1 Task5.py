tiles = open("tiles.txt").read().split('\n')
#function canBeMade defined to validate if a word can be made from the given list
def canBeMade(word, myTiles):
    for letter in word:
        if letter.upper() not in myTiles:
            return False
            break
        else:
            myTiles.remove(letter.upper())
    return True
print(canBeMade('SWET', ['T','Y','S','E','U','W','I']))