##def series(n):
##    for i in range(n):
##        yield 2**n
##        n+=1
##
##cn = series(4)


##def factorial(n):
##    for i in range(1,8):
##        n *= i
##        yield n
##cn = factorial(1)
##


def tuple1(n):
    t = ()
    for i in range(n):
        t = t+ (i, 2**(i-1))
        yield t

cn = tuple1(8)
