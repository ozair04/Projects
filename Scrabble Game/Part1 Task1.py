#scores read into a dictionary, new lines removed
scores = {line.split()[0] : line.split()[1] for line in open("scores.txt")}
#tiles and dictionary read into lists,new lines removed
tiles = open("tiles.txt").read().split('\n')
dictionary = open("dictionary.txt").read().split('\n')
