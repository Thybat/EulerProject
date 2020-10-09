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
    l=[]
    x=2
    l.append(2)
    while(x<=max):
        if(prime(x)==True):
            l.append(x)
        if x>math.ceil(pow(max,1/2)):
            return l
        x=x+1
    return l

def return_first(x):
    l=prime_list(x)
    i=len(l)-1
    while i>=0:
        if x%l[i]==0:
            return l[i]
        i=i-1
print(return_first(317584931803))
print(time.time()-start)
   
