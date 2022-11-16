

def Vigenere_Reader(file, key):
    r = open(file, 'r')
    file = r.read().split('\n')
    message = ''.join(file)
    encrypt = encryption(message, key)
    print('The Encryption of: ' + message)
    print('is ;' + encrypt)
    print()
    print()
    decryption_key = decryption(encrypt, key)
    print('The decryption using the key is: ' + decryption_key)
    print()
    print()
    decrypt = dictionaryA(encrypt)
    print(decrypt)
    
    

def Vigenere(text, key, encrypt =True):
    if encrypt == True:
        encrypted = encryption(text, key)
        return encrypted
    else:
        decrypted = decrypt(text, key)
        return decrypted
        
def encryption(message, key):
    cipher = ''
    file = message.lower()
    index = 0
    for c in file:
        if c.isalpha():
            offset = ord(key[index]) - ord('a')
            encrypted = chr((ord(c) - ord('a')+offset) % 26 + ord('a'))
            cipher += encrypted

            index = (index + 1) % len(key)
        else:
            cipher += c
    return cipher

def decryption(cipher, key):
    plaintext = ''
    index = 0

    for c in cipher:
        if c.isalpha():
            offset = ord(key[index]) - ord('a')
            decrypt = ord(c) - ord('a') - offset
            if decrypt < 0:
                decrypt += 26
            decrypted = chr( decrypt + ord('a'))

            plaintext += decrypted
            index = (index + 1) % len(key)
        else:
           plaintext += c 
    return plaintext    

#Frequency Analaysis -----------------------------------------------------------
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
englishLetterFreq = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97,
                      'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25,
                      'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36,
                      'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.29,
                      'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10,
                      'Z': 0.07}
def getLetterCount(message):
    letterCount = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0,
                   'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0,
                   'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0,
                   'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}

    for letter in message.upper():
        if letter in letters:
            letterCount[letter] += 1

    return letterCount

def getItemAtIndexZero(x):
    return x[0]

def getFrequencyOrder(message):
    letterToFreq = getLetterCount(message)
    freqToLetter = {}
    freqOrder =[]
    
    for letter in letters:
        if letterToFreq[letter] not in freqToLetter:
            freqToLetter[letterToFreq[letter]] = [letter]
        else:
            freqToLetter[letterToFreq[letter]].append(letter)

    for freq in freqToLetter:
        freqToLetter[freq].sort(key=ETAOIN.find,reverse=True)
        freqToLetter[freq] = ''.join(freqToLetter[freq])

    freqPairs = list(freqToLetter.items())
    freqPairs.sort(key=getItemAtIndexZero, reverse=True)
    
    for freqPair in freqPairs:
        freqOrder.append(freqPaiger[1])

    return getletterCount(message)
    return ''.join(freqOrder)

#Dictionary Attack decryption ---------------------------------------------------
def dictionary():
    dictionary = open('/Users/kiansilva/Desktop/dictionary.txt', 'r')
    words = dictionary.readlines()
    dictionary.close()
    
def dictionaryA(cipher):
    text = ''
    words = dictionary()

    for i in words:
        word = words.strip('\n')
        decryptedText = decryption(cipher, word[i])
        text = decryptedText.split()
        if wordCheck(text):
            return decryptedText

def wordCheck():
    words = dictionary()
    i = 0
    if (i < len(text)):
        if text[i] in words:
            i += 1
        else:
            return false
    elif i == len(text):
        return true
        
        
    
            
            
   
