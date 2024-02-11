##d1 = {}
##l=[]
##ch = "y"
##while ch == "y": 
##    key = input("Enter the key: ")
##    if key == "End":
##        break
##    value = eval(input("Enter the value: "))
##    d1[key] = value
##print(d1)
####team = input("Enter the team name: ")    
####for key in d1:
####    if key == team:
####        perc = d1[key][0] / ((d1[key][0]+d1[key][1]))*100
####print (perc)    
####for key in d1:
####   l.append(d1[key][0])
####print (l)
####    
##for key in d1:
##    if d1[key][0]>d1[key][1]:
##        l.append(key)
##print (l)


##d1 = {}
##ch = "y"
##flag =1
##while ch == "y": 
##    key = input("Enter the product: ")
##    if key == "End":
##        break
##    value = eval(input("Enter the price: "))
##    d1[key] = value
##search = input("Enter the product name: ")
##while ch=="y":
##    for key in d1:
##        if search==key:
##            print(d1[key])
##            flag = 1
##            break
##        else:
##            continue
##    if flag == 0:
##       print("Product not found")
##    flag  = 0
##    search = input("Enter the product name: ")
##
##
##d1 = {"Jan" : 31 , "Feb" : 28, "Mar" : 31, "Apr" : 30, "May" : 31, "June": 30,
##      "July" : 31, "Aug" : 31, "Sep" : 30, "Oct" : 31, "Nov" : 30, "Dec" :31}
##l = list(d1.keys())
##l.sort()
##print(l)

##
##
##for keys in d1:
##    if d1[keys]==31:
##        print (keys)


##d1 = {'k1':'v1', 'k2':'v2' , 'k3':'v3'}
##d2={}
##for key in d1:
##    value = d1[key]
##    d2[value] = key
##print(d2)

##d1 = eval(input("Enter: "))
##d2 = eval(input("Enter: "))
##l1=[]
##for i in d1:
##    for j in d2:
##        if i==j:
##            l1.append(i)
##print (l1)


##d1 = eval(input("Enter: "))
##count =0
##for key in d1:
##    count = 0
##    for key1 in d1:
##        if d1[key] == d1[key1]:
##            count += 1
##if count >= 2:
##    print("Similar",count)
##else:
##    print("Not FOund")
##    
