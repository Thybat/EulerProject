import numpy as np
import math
import time
start=time.time()
def get_str():
    names=np.loadtxt("names.txt",dtype=str,delimiter=',')
    l=[]
    for s in names:
        l.append(s[1:len(s)-1])
    sorted_l= sorted(l)
    return sorted_l
def calculate():
    l=get_str()
    somme=0
    list_somme=[]
    for s in l:
        somme=0
        for i in range(0,len(s)):
            somme=(ord(s[i])-64)+somme
        list_somme.append(somme)
    return  list_somme
def mult():
    l=calculate()
    somme=0
    for i in range(0,len(l)):
        somme=(i+1)*(l[i])+somme
    return somme
print(mult())
print(time.time()-start)