##class Pratham(Exception):
##    def __init__(self,e):
##        self.message = e
##    pass
##
##myError1= Pratham("Invalid")
##myError2 = Pratham("Invalid")
##class Time():
##    def __init__(self, hrs, minutes):
##        self.hrs = hrs
##        self.minutes = minutes
##
##    def hours(self):
##        try:    
##            if self.hrs != 0.23:
##                print("passed")
##            else:
####                raise myError1
##                raise Pratham("Error in hours")   ## Another Way
##
##        except Pratham as a:
##            print (a.message, ": Entered value: ", self.minutes)
##
##        finally:
##            print("Ok, done with hours")
##
##    def minutes1(self):
##        try:
##            if self.minutes != 0.23:
##                print("passed")
##            else:
####                raise myError2
##                raise Pratham("Error in minutes")
##
##        except Pratham as b:
##            print (b.message, ": Entered value: ", self.minutes)
##
##        finally:
##            print("Ok, done with minutes")
##
##
##ob1  = Time(0.23,0.24)
##ob1.hours()
##ob1.minutes1()



##class Pratham(Exception):
##    def __init__(self,e):
##        self.message = e
##    pass
##
##myError1= Pratham("Invalid")
##
##class Student:
##    def __init__(self, age, marks, perc):
##        self.age = age
##        self.marks = marks
##        self.perc = perc
##
##    def age1(self):
##
##        while True:
##            try:
##                self.age = int(input("Enter the age:"))
##                break
##            except ValueError:
##                print("Invalid")
##                
##        print("Age Entered")
##
##    def marks1(self):
##        while True:
##            try:
##                self.marks = eval(input("Enter the marks of 3 sub:"))
##                if len(self.marks) ==3:
##                    break
##            except IndexError:
##                print("Enter the marks for 3 sub only")
##        print("Mark's entered")
##
##    def perc1(self):
##        sum1 = 0
##        while True:
##            try:
##                a = int(input("Enter the total number of sub: "))
##                if a !=3:
##                    raise myError1
##                else:  
##                    for i in self.marks:
##                        sum1 = sum1 + i
##                    self.perc = sum1/a
##                    print("Percentage calculated")
##                    break
##            
##            except ZeroDivisionError:
##                print("Total number of subjects cannot be zero")
##
##            except Pratham as a:
##                print(a.message, ", Total number of subjects can only be 3")
##
##
##ob1  = Student(0,[],0)
##ob1.age1()
##ob1.marks1()
##ob1.perc1()


