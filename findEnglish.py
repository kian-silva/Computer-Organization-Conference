LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz \t\n'

def loadDictionary():
    dictionaryFile = open('/Users/kiansilva/Desktop/dictionary.txt', 'r')
    englishWords = {}
    for word in dictionaryFile.read().split('\n'):
        englishWords[word] = None
    dictionaryFile.close()
    return englishWords

English_words = loadDictionary()

def getEnglishCount(message):
    message = message.upper()
    message = removeNonLetters(message)
    possibleWords = message.split

    if possibleWords == []:
        return 0.0 #no words present

    mathches = 0
    for word in possibleWords:
        if word in English_Words:
            matches+= 1
            return float(matches)/len(possibleWords)

def removeNonLetters(message):
    OnlyLetters = []
    for symbol in message:
        if symbol in Letters_Space:
            OnlyLetters.append(symbol)
    return ''.join(OnlyLetters)

def isEnglish(message, wordPercentage=20, letterPercentage=85):
 #20% of the words must exist in the dictionary file, and
 #85% of all the characters in the message must be letters or spaces
    words = getEnglishCount(message)* 100 >= wordPercentage
    numLetters = len(removeNonLetters(message))
    messageLettersPercentage = float(numLetters)/len(message) * 100
    lettersMatch = messageLettersPercentage >= letterPercentage
    return words and letterMatch

