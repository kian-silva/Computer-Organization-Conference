def atbash(message):
    code = ""
    message = message.lower()
    word = ""
    a = 0
    i = 0
    while a < len(message):
        if message[a].isalpha():
            word += message[a]
            a+= 1
        else:
            a +=1
    while i < len(word):
        char = word[i]
        old_char = ord(char) - ord("a")
        new_char = -(old_char + 1) % 26
        code += chr(new_char + ord("a"))
        i += 1
    return code
