import math
import time
start=time.time()
def nbr_sundays():
    sundays=0
    tab=[31,28,31,30,31,30,31,31,30,31,30,31]
    i=2
    year_cnt=False
    for y in range (1901,2001,+1):
        
        if y%4==0 and y%100!=0:
            year_cnt=True
        elif y%400==0:
            year_cnt=True
        else:
            year_cnt=False
        if year_cnt==True:
            tab[1]=29
        elif year_cnt==False:
            tab[1]=28

        for s in range (0,12):
                i=i+tab[s]
                if i%7==0:
                    sundays=sundays+1

    return sundays
print(nbr_sundays())
print(time.time()-start)
