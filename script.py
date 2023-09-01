def decoupeChaine(str):
    result = ""
    for i in range(0, len(str)):
        if str[i] != str[i -1]:
            result += " "
        result += str[i]
    return result.strip()

print(decoupeChaine("ab"))

def decritChaine(chaine):
    str_decouper = decoupeChaine(chaine)
    tab = str_decouper.split(" ")
    result = ""
    for i in range(0, len(tab)):
        result += str(len(tab[i])) + tab[i][0]
    return result

print(decritChaine("aabbbggtkhh"))

def suiteConway(chaine, n):
    for k in range(1, n):
        print(chaine)
        chaine = decritChaine(chaine)
        
    return chaine

print(suiteConway("a", 3))