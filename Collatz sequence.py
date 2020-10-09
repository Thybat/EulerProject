import math
import time
start=time.time()
def collatz(start):
    i=1
    while(start>1):
        if start%2==0:
            start=start//2
        else:
            start=start*3+1
        i=i+1
    return i
def max_collatz():
    s=0
    max=0
    fly_time=0
    collatz_nmber=0
    for s in range(1,1000000,+1):
        collatz_nmber=collatz(s)
        if collatz_nmber>fly_time:
            fly_time=collatz_nmber
            max=s
    return max
print(max_collatz())
print(time.time()-start)
