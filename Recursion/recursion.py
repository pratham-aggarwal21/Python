##def prime(n, divisor=2):
##    if n % divisor == 0:
##        return False
##    elif divisor * divisor > n:
##        return True
##    else:
##        return prime(n, divisor + 1)
##
##print(prime(7))

##def product(x, y):
##    if y == 0:
##        return 0
##    elif y > 0:
##        return x + product(x, y - 1)
##print(product(3,3))


##def hailstone(n):
##    l =[]
##    if n==1:
##        return l
##    elif n%2==0:
##        l.append(n)
##        return l + hailstone(int(n/2))
##    else:

##        l.append(n)
##        return 3*hailstone(n+1)
##print(hailstone(100))

##def adm(adm_list, target, low, high):
##    if low<=high:
##        mid = int((low + high)/2)
##
##        if adm_list[mid] == target:
##            return True
##        elif adm_list[mid] < target:
##            return adm(adm_list, target, mid + 1, high)
##        else:
##            return adm(adm_list, target, low, mid - 1)
##    else:
##        return False
##
##admList = [1,2,3,4,5,6,7,8,9,10]
##print(adm(admList, 1, 0, len(admList)-1))

def reverse(x):
    if x==0:
        return x
    else:
        reverse(x-1)
        print (x)
reverse(10)


