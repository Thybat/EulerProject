import math
import numpy as np

d = 0

def tab_need():
    tab=[]

    for i in range (0,1000):
        sqr = math.sqrt(i)
        if sqr-math.floor(sqr)!=0:
            tab.append(i)
    return tab
def diophantine(d):
    for i in range(1,50000):
        for s in range(1,50000):
            if s*s-(d*i*i)==1:
                return s
def sort_result():
    tab=tab_need()
    result=[]
    somme=0
    stock=0
    for i in tab:
        print(i)
        stock=diophantine(i)
        if stock>somme:
            somme=stock
            result.append(somme)

    print (result[-1])
sort_result()
#l=diophantine()
#print(l[-1])