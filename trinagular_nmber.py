import time
import math
import numpy as np
start=time.time()
def triangular_nmber():
    somme=0
    i=1
    sqrt=0
    l=[]
    while(len(l)<500):
        somme=somme+i
        l.clear()
        nbr_div=2
        if somme%2==0:
            l.extend([1,somme])
            sqrt=math.ceil(math.sqrt(somme))
            for s in range (2,sqrt,+1):
                if somme%s==0:
                    l.extend([s,somme//s])

                             
        i=i+1
    return l
print(triangular_nmber())
print(time.time()-start)
