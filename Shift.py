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
        statement += chr((ord(char) + s - 97) % 26 + 97)
    return statement
