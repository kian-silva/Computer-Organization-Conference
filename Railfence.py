

def railfence(statement):
    stat = ''
    phrag1 = ''
    phrag2 = ''
    a = 0
    e = 0
    while a < len(statement):
        if statement[a].isalpha():
            stat += statement[a]
            a+= 1
        else:
            a +=1
    while e < len(stat):

        if e % 2 == 0:
            phrag1 += stat[e]
        else:
            phrag2 += stat[e]

        e += 1
    
    return phrag1 + phrag2

