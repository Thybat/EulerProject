import math

def sum_digit_fibo():
    tab = [1, 2]
    i=2
    while(True):
        tab.append(tab[i-1]+tab[i-2])
        string=str(tab[i])
        if len(string) ==1000:
            print(string)
            return i+2
            break
        i=i+1


print(sum_digit_fibo())
