str_int=[]
str = "" #MET L'ENIGME ICI ! 
for i in range (0, len(str)):
    print(str[1])
    if (ord(str[i])<=122) and (ord(str[i]) >= 99):
        str_int.append(ord(str[i])-2)
    elif (ord(str[i]) == 32):
        str_int.append(32)
print(''.join(chr(i) for i in str_int))


