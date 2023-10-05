scores = {line.split()[0] : line.split()[1] for line in open("scores.txt")}
#function getLetterScore is required for each letter in the word
def getLetterScore(letter):
    if letter.upper() not in scores.keys():
        score = 0
    else:
        score = scores.get(letter.upper())
    return score
#function getWordScore defined to return score for a given word
def getWordScore(word):
    #total variable made to tally the scores of letters in the word
    total = 0
    for i in word:
        total += int(getLetterScore(i))
    return total
print(getWordScore('MOSHI'))
