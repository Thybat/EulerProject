import time
import math
import numpy as np
import pandas as pd
from collections import Counter
start=time.time()
def amicable():
    sqrt=0
    tab=np.zeros((300,50), dtype=int)
    for i in range(1,300):
        nbr_div=2
        y = 1
        for s in range (1,i+1,+1):
            if i%s==0:
                tab[i][y]=s
                y = y + 1
    return tab
def sum_list():
    tab=amicable()
    tab=np.sum(tab, axis=1)
    print(tab)

print(sum_list())

print(time.time()-start)
