import math
import time
start =time.time()
def exoPuiss2(x):
    num=1
    for i in range(1,x+1):
        num=2*num
    return num
def sum_pow(x):
    string=str(exoPuiss2(x))
    size=0
    somme=0
    size=len(string)
    for i in range(0,size):
        somme=int(string[i])+somme

    return somme
print(sum_pow(1000))
print(time.time()-start)
