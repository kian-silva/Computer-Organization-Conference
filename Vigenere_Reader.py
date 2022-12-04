
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
    key = key.lower()
    for i in cipher:
        if i.isalpha():
            offset = ord(key[index]) - ord('a')
            decrypt = (ord(i) - ord('a') - offset) % 26
            decrypted = chr( decrypt + ord('a'))

            plaintext += decrypted
            index = (index + 1) % len(key)
        else:
           plaintext += i 
    return plaintext    


#Dictionary Attack decryption ---------------------------------------------------
def dictionary():
    dictionary = open('/Users/kiansilva/Desktop/dictionary.txt', 'r')
    words = dictionary.readlines()
    dictionary.close()
    return words

def CommonWords():
    common = open('/Users/kiansilva/Desktop/Most_common_words.txt', 'r')
    commonWords = common.readlines()
    common.close()
    return commonWords
    
def dictionaryAttack(cipher):
    text = ''
    words = dictionary()
    commonWords = CommonWords()
    
    for i in commonWords:
        print(i)
        decrypt = decryption(cipher, i)
        print(decrypt)
        if wordCheck(words, decrypt):
            return decryptedText
            

        
def wordCheck(words, text):
    i = 0
    while (i < 5):
        if text[i] in words:
            print(text[i])
            i += 1
        else:
            return False
        if i == len(text):
            return True
        
        
    
            
            
   
