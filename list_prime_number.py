import time
import math
start = time.time()

def prime(prime, list):
    i = 2
    sqr_prime = math.ceil((pow(prime,1/2)))
    while i <= sqr_prime:
        if prime % i == 0:
            return False
        i = i+1
    return True
def prime_list(max):
    x=3
    list =[]
    list.append(2)
    while(x<=max):
        if(prime(x, list)==True):
            list.append(x)
        x=x+2
    return list

print(len(prime_list(180000)))
print(time.time()-start)
