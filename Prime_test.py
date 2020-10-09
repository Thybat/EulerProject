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
print(prime(170141183460469231731687303715884105727))
print(time.time()-start)
