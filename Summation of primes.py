import time
import math
start = time.time()

def prime(prime):
    i=2
    sqr_prime=math.ceil((pow(prime,1/2)))
    while i<=sqr_prime:
        if prime%i==0 and prime!=i:
            return False
        i=i+1
    return True
def prime_list(max):
    x=2
    somme=0
    while(x<=max):
        if(prime(x)==True):
            somme=somme+x
        x=x+1
    return somme

print(prime_list(2000000))
print(time.time()-start)
