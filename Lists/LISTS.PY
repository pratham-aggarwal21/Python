##l=[8,9,10]
##l[1]=17
##l.insert(len(l),4)
##l.insert(len(l),5)
##l.insert(len(l),6)
##print(l)
##l.pop(0)
##l.sort()
##i=0
##for i in range(len(l)):
##    l[i]=l[i]*2
##l.insert(25,3)
##print(l)

##
##l=eval(input("Enter list elements:"))
##i=0
##for i in range(len(l)):
##    if l[i]>10:
##        l[i]=10
##print(l)

##l=eval(input("Enter list elements: "))
##newList = []
##for word in l:
##    newWord  = word[1:]
##    newList.append(newWord)
##print(newList)

##l1 = []
##for i in range(50):
##    l1.append(i)
##print (l1)
##
##
##l2=[]
##for j in range(1,51):
##    j = j*j
##    l2.append(j)
##print(l2)
##
##l3 = []
##for j in range(26):
##    string = chr(97 + j) * (j + 1)
##    l3.append(string)
##
##print(l3)

##l1 = eval(input("Enter the elements of the first list: "))
##l2 = eval(input("Enter the elements of the second list: "))
##newList = []
##for i in range(len(l1)):
##    newList.append(l1[i]+l2[i])
##print(newList)

##n=int(input("Enter nth value: "))
##a=0
##b=1
##if n==1:
##    result = a
##elif n==2:
##    result = b
##else:
##    c=2
##    while c<=n:
##        result = a+b
##        a = b
##        b=result
##        c += 1
##print (result)

##
##l=eval(input("Enter: "))
##last=l[-1]
##for i in range(len(l)-1,0,-1):
##    l[i] = l[i-1]
##l[0] = last
##print (l)
##

##l=eval(input("Enter: "))
##longest = len(l[0])
##for i in l:
##    if len(i)>longest:
##        longest = len(i)
##        longest_word = i
##print (longest_word)

l=eval(input("Enter: "))

for i in range (len(l)):
    l[i] = l[i]+i
print(l)
