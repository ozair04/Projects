scores = {line.split()[0] : line.split()[1] for line in open("scores.txt")}
#function getLetterScore defined to return a score for a given letter
def getLetterScore(letter):
    #scans through the dictionary of scores to find the score for the letter
    if letter.upper() not in scores.keys():
        score = 0
    else:
        score = int(scores.get(letter))
    return score

