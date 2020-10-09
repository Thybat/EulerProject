def smallest(x):
    i=20
    while i>0:
        if x%i!=0:
            return 0
        i=i-1
    return x
i=0
while(True):
    if smallest(i)!=0:
        print(i)
        break
    i=i+1
    

