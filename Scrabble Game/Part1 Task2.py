#alphabet variable made
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#function onlyEnglishLetters defined to allow only elements from alphabet variable
def onlyEnglishLetters(word):
    for letter in word:
        if letter.upper() not in alphabet:
            result = False
            break
        else:
            result = True
    return result


