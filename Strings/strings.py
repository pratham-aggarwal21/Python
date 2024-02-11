## Q1
##s = input ("Enter a number: ")
##if s[0:3].isdigit() and s[3] == '-' and s[4:7].isdigit() and s[7] == '-' and s[9:].isdigit() and len(s[9:])=='4':
##    print("Valid")
##else:
##    print("Invalid")

##Q2
##s = input ("Enter a string")
##sum = 0
##f=1
##for ch in s:
##    if ch.isdigit():
##        print(ch, end=" ")
##        sum = sum + int(ch)
##        f=0
##if f==1:
##    print("No digits")
##else:
##    print (sum)


##Q3
##s=input("Enter a string:")
##l=s.split(" ")
##character =0
##space =0
##alphanum =0
##for ch in s:
##    character = character +1
##    if ch.isalnum():
##        alphanum = alphanum+1
##        
##per = (alphanum/len(s))*100
##print(character)
##print(len(l))
##print(per)


##Q4
##while True:
##    s= input("Enter a sentence: ")
##    if s!='q':
##        for ch in s:
##            if ch.islower():
##                print(ch.upper(), end="")
##            elif ch.isupper():
##                print(ch.lower(), end="")
##            elif ch == " ":
##                print(end = " ")
##        else:
##            print(" ")
##            
##    else:
##        break


##Q5
##i= input ("Enter an integer: ")
##s = input ("Enter a string: ")
##sum=0
##f=0
##n=""
##for ch in s:
##    if ch.isdigit():
##        n = n + ch
##        f=1
##if f==0:
##    n = 0
##sum= int (n)+ int(i)
##print (n, "+", i, "=", sum)



str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

if len(str1) <= len(str2):
    smaller_str = str1
    larger_str = str2
else:
    smaller_str = str2
    larger_str = str1


print(smaller_str)


for i in range(len(larger_str)):
    


