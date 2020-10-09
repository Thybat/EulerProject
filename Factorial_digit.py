import math
def fact(x):
    fact=x
    while(x>1):
        x=x-1
        fact=fact*x
        
    return fact
def sum_digit(x):
    string=str(fact(x))
    size=0
    somme=0
    size=len(string)
    for i in range(0,size):
        somme=int(string[i])+somme
    return somme
print(sum_digit(100))
