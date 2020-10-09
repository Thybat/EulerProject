import numpy as np
import math
import time
from functools import reduce
somme=0
somme1=0
tab=np.loadtxt('largest.txt', dtype=str, delimiter=',')

l=[]

for s in range (0,20):
    for i in range(0,50):
        l.append(int(tab[s][i]))
for s in range(0,1000-13):
    somme1=reduce(lambda x, y:x*y, l[0+s:13+s])
    if somme1>somme:
        somme=somme1
print(somme)
