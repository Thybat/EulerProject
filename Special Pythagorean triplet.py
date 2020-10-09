import math
import time
start=time.time()
def pythagore():
    a=0
    b=0
    a2=0
    b2=0
    c=0
    sqrt=0
    somme=0
    for a in range(1,1000):
        a2=a*a
        for b in range(1,1000):
            b2=b*b
            c=a2+b2
            sqrt=int(math.sqrt(c))
            if c==sqrt*sqrt:
                somme=a+b+sqrt
                if somme==1000:
                        print(a,b,sqrt)
                        return a*b*sqrt
            
print(pythagore())
print(time.time()-start)
