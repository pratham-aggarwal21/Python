##def conversion(dollar):
##    rupees = dollar*85
##    return rupees
##a = int(input("Enter the ammount in dollar: "))
##converted = conversion(a)
##print(converted)


##def volume(l,b,h):
##    Calc_volume = l*b*h
##    return Calc_volume
##length  = int(input("Enter the length: "))
##Width  = int(input("Enter the width: "))
##Height  = int(input("Enter the height: "))
##a = volume(length, Width, Height)
##print(a)


##def cube(a=2,b=2):
##    c1 = a*a*a
##    c2 = b*b*b
##    print(c1,c2)
##a=20
##b=30
##cube(a,b)


##def equal(a,b):
##    if a==b:
##        return True
##    else:
##        return False
##a='H'
##b='B'
##c = equal(a,b)
##print(c)

##import random
##def randomNum(a,b):
##    c = random.randint(a,b)
##    return c
##    
##a=10
##b=20
##c = randomNum(a,b)
##print(c)

##import math
##def nthRoot(x,y):
##    return pow(x,1/y)
##print(nthRoot(20,1))

##import random
##import math 
##def genrandom(n):
##    return random.randint(pow(10,(n-1)),(pow(10,n))-1)
##print(genrandom(4))

##def minimum(x,y):
##    if (x%10 < y%10):
##        return x
##    else:
##        return y
##print(minimum(491, 278))

##def series(x,y):
##    a = (x+y)/4
##    t=[x]
##    while x+a<=y:
##        x = x+a
##        t.append(int(x))
##    return t
##print(series(1,11))

##def checkLen(x,y):
##    if len(x)==len(y):
##        return True
##    else:
##        return False
##print(checkLen("Hello1","World"))
