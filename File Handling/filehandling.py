##WAP to reead the contents of the file and count the number of letters, exclude spaces.
##
##WAP to reead the contents of the file and counts the number of vovels
##
##count number of capital vovels, small vovels, capital consonents, lowercase consonents, digits, special symbols
##
##WAP that copies contents of one file to another
##
##WAP that copies those lines into second file which are beginning from vovels
##
##Given a list with numbers, transfer all odds to odd.txt and even to even.txt
##
##count number of words in given file
##
##count numebr of words ending with vovel

##myfile =open("Test.txt","r")
##str1 = ' '
##count =0 
##while str1:
##    str1 = myfile.read(1)
##    count +=1
##print(count)

##myfile =open("Test.txt","r")
##str1 = ' '
##count =0 
##while str1:
##    str1 = myfile.read(1)
##    if str1 in "AaeEiIoOuU":
##        count += 1
##print(count)


##myfile =open("Test.txt","r")
##str1 = ' '
##UpperV =0
##LowerV = 0
##UpperC= 0
##LowerC = 0
##special = 0
##digits = 0
##while str1:
##    str1 = myfile.read(1)
##    if str1.islower():
##        if str1 in "aeiou":
##            LowerV += 1
##        else:
##            LowerC += 1
##    elif str1.isupper():
##        if str1 in "AEIOU":
##            UpperV += 1
##        else:
##            UpperC += 1
##    elif str1.isdigit():
##        digits += 1
##    else:
##        special +=1
##        
##print(UpperV)
##print(LowerV)
##print(UpperC)
##print(LowerC)
##print(special)
##print(digits)



##myfile = open("Test.txt", "r")
##myfile2 = open("Test1.txt", "w")
##str1 =' '
##while str1:
##    str1 = myfile.read(1)
##    myfile2.write(str1)
##myfile2.close()
##print("File created")


##myfile = open("Test.txt", "r")
##myfile2 = open("Test2.txt", "w")
##str1 =" "
##while str1:
##    str1 = myfile.readline()
##    for i in str1:
##        if i in "AaEeIiOoUu":
##            myfile2.write(str1)
##        else:
##            break
##myfile2.close()
##print("File created")


##l1 = [1,2,3,4,5,6,7,8,9,10]
##myfile = open("Odd.txt", "w")
##myfile2 = open("Even.txt","w")
##
##for i in l1:
##    if i%2==0:
##        myfile2.write(i)
##    else:
##        myfile.write(i)
##myfile.close()
##myfile2.close()
##print("Files created")


##myfile =open("Test.txt","r")
##str1 = ' '
##count =0 
##while str1:
##    str1 = myfile.readline()
##    for i in str1:
##        if i == " ":
##            count += 1
##print(count)


##myfile =open("Test.txt","r")
##str1 = ' '
##count =0 
##while str1:
##    str1 = myfile.readline()
##    l = str1.split(" ")
##    for i in l:
##        if len(i) != 0:
##            if i[-1] in "aAeEiIOoUu":
##                count += 1
##print(count)


