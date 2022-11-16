

def railfence(statement):
    phrag1 = ''
    phrag2 = ''
    e = 0
    lines = nospace(statement)
    while e < len(lines):
        if e % 2 == 0:
            phrag1 += lines[e]
        else:
            phrag2 += lines[e]

        e += 1
    
    return phrag1 + phrag2


def nospace(statement):
    a = 0
    stat = ''
    while a < len(statement):
        if statement[a].isalpha():
            stat += statement[a]
            a+= 1
        else:
            a +=1
    return stat
