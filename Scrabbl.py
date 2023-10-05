print('single player scrabble game'.title().center(100))

#scores, tiles and dictionary variables made
scores = {line.split()[0] : line.split()[1] for line in open("scores.txt")}
tiles = open("tiles.txt").read().split('\n')
dictionary = open("dictionary.txt").read().split('\n')

#alphabet variable made
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#function onlyEnglishLetters defined to allow words with only English letters
def onlyEnglishLetters(word):
    for letter in word:
        if letter.upper() not in alphabet:
            result = False
            break
        else:
            result = True
    return result

#function canBeMade defined to validate if a word can be made from the given list of tiles
def canBeMade(word, myTiles):
    for letter in word:
        if letter.upper() not in myTiles:
            return False
            break
        else:
            myTiles.remove(letter.upper())
    return True

#function isValid defined to validate if the word is viable for the game
def isValid(word, myTiles, dictionary):
    if onlyEnglishLetters(word) == True:
        if word.upper() in dictionary:
            if canBeMade(word, myTiles) == True:
                return True
            else:
                return "This cannot be made from these tiles"
        else:
            return "There is no such word in the dictionary"
    else:
        return "Only use English letters..."

#function getLetterScore defined to return scores of a letter
def getLetterScore(letter):
    if letter.upper() not in scores.keys():
        score = 0
    else:
        score = scores.get(letter.upper())
    return score

#function getWordScore defined to return total score of a word
def getWordScore(word):
    total = 0
    for i in word:
        total += int(getLetterScore(i))
    return total

#start of game
print('Generating Random Tiles...')
#variable myTiles created to append tiles to
myTiles = []
import random
#strings tiles_line and scores_line made to print tiles and scores
tiles_line = "Tiles:  "
scores_line = "Scores: "
for i in range(7):
    chosen = random.randint(0, 99)
    myTiles.append(tiles[chosen])
    tiles_line += tiles[chosen] + ' '
    scores_line += str(getLetterScore(tiles[chosen])) + ' '
print(tiles_line)
print(scores_line)
game = True
#while loop made to allow the game to repeat if word is not valid and allows user to quit
while game == True:
    word = input("Enter a word: ")
    if word == "&&&":
        print("Thanks for using this application, better luck next time!!!")
        break
    if isValid(word, myTiles, dictionary) == True:
        print("You got it right, this is a valid word")
    else:
        print(isValid(word, myTiles, dictionary))
        continue
    score = getWordScore(word)
    print("Score of this word is:", score)
    break







