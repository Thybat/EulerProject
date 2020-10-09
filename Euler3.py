import time
import math
start = time.time()

def prime(prime):
    i=math.ceil((pow(prime,1/2)))
    while i>2:
        if prime%i==0:
            return False
        i=i-1
    if i==2 and prime%2==0:
        return False
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
print(return_first(600851475143))
print(time.time()-start)
    
