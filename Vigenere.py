def Vigenere(text, key, encrypt=True):
    table = create_vigenere_table()
    key_map = ""
    j =0
    for i in range(len(text)):
        if ord(text[i]) == 32:
            key_map += " "
        else:
            if j < len(key):
                key_map += key[j]
                j += 1
            else:
                j = 0
                key_map += key[j]
                j += 1
    if encrypt == True:
        encrypted_text = ""
        for i in range(len(text)):
            if text[i] == chr(32):
                encrypted_text += " "
            else:
                row = ord(text[i])-65
                column = ord(key_map[i]) - 65
                encrypted_text += table[row][column]
        print(encrypted_text)
    else:
        decrypted_text = ""
        for i in range(len(text)):
            if text[i] == chr(32):
                decrypted_text +=" "
            else:
                decrypted_text += chr(65 + counter(ord(key_map[i]), ord(text[i])))
        print (decrypted_text)
                       
def counter(key_map, text):
    count = 0
    result = ""
    for i in range(26):
        if key_map + i > 90:
                result += chr(key_map+(i-26))
        else:
                result += chr(key_map+i)
    for i in range(len(result)):
        if result[i] == chr(text):
            break
        else:
            count+=1
    return(count)
    
def create_vigenere_table():
    table = []
    for i in range(26):
        table.append([])
    for row in range(26):
        for column in range(26):
            if (row + 65) + column > 90:
                table[row].append(chr((row+65) + column - 26))
            else:
                table[row].append(chr((row+65)+column))
    return table
