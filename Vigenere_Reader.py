
import string
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def Vigenere_Reader(file, key):
    r = open(file, 'r')
    file = r.read().split('\n')
    message = ''.join(file)
    statement = filterChar(message)
    encrypt = encryption(statement, key)
    print('The Encryption of: ' + message)
    print('is ;' + encrypt)
    print()
    print()
    decryption_key = decryption(encrypt, key)
    print('The decryption using the key is: ' + decryption_key)
    print()
    print()
    decrypt = dictionaryAttack(encrypt)
    print(decrypt)


def filterChar(file):
    message = file.translate(str.maketrans('','',string.punctuation))
    return message
        

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
    key = key.lower()
    keys = ''
    a = 0
    while a < len(key):
        if key[a].isalpha():
            keys += key[a]
            a += 1
        else:
            a += 1
    for c in file:
        if c.isalpha():
            offset = ord(keys[index]) - ord('a')
            encrypted = chr((ord(c) - ord('a')+offset) % 26 + ord('a'))
            cipher += encrypted

            index = (index + 1) % len(keys)
        else:
            cipher += c
    return cipher

def decryption(cipher, key):
    plaintext = ''
    index = 0
    key = key.lower()
    keys = ''
    a = 0
    while a < len(key):
        if key[a].isalpha():
            keys += key[a]
            a += 1
        else:
            a += 1
    for i in cipher:
        if i.isalpha():
            offset = ord(keys[index]) - ord('a')
            decrypt = (ord(i) - ord('a') - offset) % 26
            decrypted = chr(decrypt + ord('a'))

            plaintext += decrypted
            index = (index + 1) % len(keys)
        else:
           plaintext += i 
    return plaintext    


#Dictionary Attack decryption ---------------------------------------------------
# takes every word in the dictionary and puts it into the list 'words'
def dictionary():
    dictionary = open('Dictionary.txt', 'r')
    words = dictionary.readlines()
    dictionary.close()
    return words

# takes every word in the list of the 1000 most common words and puts it into
# the list 'commonWords'
def CommonWords():
    common = open('CommonWords.txt', 'r')
    commonWords = common.readlines()
    common.close()
    return commonWords

# takes in an encrypted message and tests through every word in the commonwords
# list to try and decrypt the message with each word in common words then checks
# the decryption to see if the first five words in the decrypted message are words
# in the dictionary. If the first five words are english words then that is the
# decrypted message
def dictionaryAttack(cipher):
    text = ''
    words = dictionary()
    commonWords = CommonWords()
        
    for i in commonWords:
        decrypt = decryption(cipher, i)
        text = decrypt.split()
        if wordCheck(text, words):
            return decrypt
        

"""
wordCheck takes in the dictionary list(which is called in the dictionaryAttack)
#function and the decrypted message and checks the decrypted message word by
# word to make sure the decrypted message is decrypted and not still encrypted
"""
def wordCheck(text, words):
    i = 0
    final = False
    
    while i < 5:
        if text[i].strip() in words:
            final = True
            break
        else:
            i += 1
    return final
            
            
   
