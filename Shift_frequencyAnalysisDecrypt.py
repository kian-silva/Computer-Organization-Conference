def shift(message,s):
    statement = ""
    message = message.lower()
    a = 0
    while a < len(statement):
        if statement[a].isalpha():
            stat += statement[a]
            a+= 1
        else:
            a +=1
    for i in range(len(message)):
        char = message[i]
        if char.isalpha():  
            statement += chr((ord(char) + s - 97) % 26 + 97)
        else:
            statement += char
    return statement


Alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'

def frequency_analysis(s):

    letterFreq = {'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0,
                  'K':0,'L':0,'M':0,'N':0,'O':0,'P':0,'Q':0,'R':0,'S':0,'T':0,
                  'U':0,'V':0,'W':0,'X':0,'Y':0,'Z':0}
    
    
    for letter in s.upper():
        if letter in Alpha:
            letterFreq[letter] +=1
    for letter in letterFreq:
        letterFreq[letter] = (letterFreq[letter]/len(s)) * 100
    letterFreq = sorted(letterFreq.items(), key=lambda x:x[1], reverse=True)
    letterFreq = dict(letterFreq)
    return letterFreq

def decryptShift(s):
    encrypted = s.upper()
    letterFreq = frequency_analysis(s)
    letter_list = list(letterFreq.keys())
    letter_str = ''.join(letter_list)
    key = Alpha.find(letter_str[0]) - Alpha.find('E')
    decrypted = shift(encrypted, - key)

    return decrypted


