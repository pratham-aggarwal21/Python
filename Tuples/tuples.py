##t= (0,)
##a=0
##b=1
##c=2
##while c<=9:
##    result = a+b
##    a = b
##    b = result
##    c += 1
##    t = t + (result,)
##print(t)

##t = eval(input("Enter: "))
##i = int(input("Enter the index: "))
##print(t[i])

##t= (0,1,1,)
##user_input = int(input("Enter: "))
##a=1
##b=1
##c=2
##while c<=user_input: 
##    result = a+b
##    a = b
##    b = result
##    c += 1
##    t = t + (result,)
##print(t.index(user_input))
##

##a = tuple()
##a1= tuple()
##t = eval(input("Enter the marks/end to exit: "))
##sum1 =0
##while t!="End":
##    a = a+(t,)
##    t = eval(input("Enter the marks/end to exit: "))
##for i in a:
##    for j in i:
##        sum1 = sum1 + j
##    a1 = a1+(sum1,)
##    sum1=0
##print(a1)


##t1 = eval(input("Enter the first tuple: "))
##t2 = eval(input("Enter the second tuple: "))
##t3 = tuple()
##t3 = t1+t2
##print(t3)


##l1=tuple()
##for j in range(1,51):
##    j = j*j
##    l1 = l1 + (j,)
##print(l1)


##l1 = tuple()
##for j in range(26):
##    string = chr(97 + j) * (j + 1)
##    l1 = l1 + (string,)
##print(l1)


##t = eval(input("Enter the tuple: "))
##count = 0
##for i in t:
##    even = True  
##    for j in i:
##        if j % 2 != 0:  
##            even = False  
##    if even == True:
##        count += 1
##print(count)


##l1 = eval(input("Enter the tuple: "))
##l2 = eval(input("Enter the tuple: "))
##if l1==l2:
##    print(True)
##else:
##    print(False)


##l1 = eval(input("Enter the tuple: "))
##sum1 =0
##i=0
##for i in l1:
##    sum1 = sum1+ i
##mean = sum1/len(l1)
##print(mean)


##l1 = eval(input("Enter the tuple: "))
##mean1 = 0
##sum1 = 0
##totalMean = 0
##
##for i in l1:
##    for j in i:
##        sum1 = sum1 + j
##    mean1 = sum1 / len(i)
##    print("Mean of inner", mean1)
##    
##    totalMean += mean1
##
##Mean = totalMean / len(l1)
##print("Mean of means:", Mean)




