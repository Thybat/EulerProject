import math
def find_palindrome():
    string=""
    mult=0
    somme=0
    for s in range (999,100,-1):
        for i in range (999,100,-1):
            mult=i*s
            string=str(mult)
            if len(string)==6:
                if string[0]==string[5] and string[1]==string[4] and string[2]==string[3] and mult>somme:
                    somme=mult
    return somme
print(find_palindrome())
