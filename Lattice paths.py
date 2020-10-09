import math
import time
import numpy as np
def lattice_paths():
    tab=np.ones((2,3), dtype=int)
    tab[1][2]=0
    print(tab)
    x=0
    y=0
    somme=0
    path=0
    while(somme!=5):
        x=0
        y=0
        if tab[x][y]!=0:
           x=x+1
    
    return path
print(lattice_paths())
