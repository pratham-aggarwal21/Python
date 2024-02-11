##class Time1:
##    def __init__(self):
##        pass
##    def convert_to_min(self, x):
##        a = int(x/60)
##        b = x%60
##        return (a,":",b)
##    def convert_to_hr(self, x):
##        a = int(x/3600) 
##        b = int((x%3600)/60)
##        c = x%60
##        return (a,":", b, ":", c)
##ob1 = Time1()
##print(ob1.convert_to_min(100))
##print(ob1.convert_to_hr(100))

##class Book:
##    def __init__(self, book_number = 0, book_name=" ", author = " ",
##                 publisher = " ", price = 0, num_of_copies = 0 , issued = 0):
##        self.book_number = book_number
##        self.book_name = book_name
##        self.author  = author
##        self.publisher = publisher
##        self.price = price
##        self.num_of_copies = num_of_copies
##        self.issued = issued
##    def issue(self):
##        self.issued = self.issued + 1
##    def display(self):
##        print(self.book_number, self.book_name, self.author, self.publisher, self.price,
##              self.price, self.num_of_copies, self.issued)
##    def rno(self):
##        return self.book_number
##
##ch = 0
##l =[]
##while ch<=3:
##    print("Press 1 for insert")
##    print("Press 2 for issue")
##    print("Press 3 for display")
##    ch = int(input("Enter your choice:"))
##    if ch==1:
##        number = int(input("Enter the book number: "))
##        name = input("Enter the book name: ")
##        publisher = input("Enter the publisher: ")
##        price = int(input("Enter the price: "))
##        num1= int(input("Enter the number of copies: "))
##        ob1 = Book(number, name, publisher, price, num1, 0)
##        l.append(ob1)
##    elif ch==2:
##        number = int(input("Enter the book number: "))
##        for i in l:
##            if i.rno()==number:
##                i.issue()
##    elif ch==3:
##        number = int(input("Enter the book number: "))
##        for i in l:
##            if i.rno()==number:
##                i.display()

##class fixedDeposits:
##    def __init__(self,name, accnum, time_period, amt):
##        self.name = name
##        self.accnum = accnum
##        self.time_period = time_period
##        self.amt = amt
##    def initialise(self):
##        self.name = input("Enter the name: ")
##        self.accnum = int(input("Enter the account number: "))
##        self.time_period = int(input("Enter the time period: "))
##        self.amt = int(input("Enter the amount to deposit: "))
##        print("Account has been initialized")
##    def withdraw(self, x):
##        self.amt = self.amt - x
##        print("Amount withdrawm")
##    def display(self):
##        print("Name: ", self.name)
##        print("Account Number: ", self.accnum)
##        print("Time period: ", self.time_period, "years")
##        print("Amount: ", self.amt)
##
##accounts = []
##while True:
##    print("1. Initialise Account")
##    print("2. Withdraw Money")
##    print("3. Display Account Details")
##    print("4. Exit")
##    choice = int(input("Enter your choice:"))
##    if choice == 1:
##        account = fixedDeposits("", 0, 0, 0)
##        account.initialise()
##        accounts.append(account)
##    elif choice == 2:
##        acc_number = int(input("Enter the account number: "))
##        withdraw_amt = int(input("Enter the amount to withdraw: "))
##        for i in accounts:
##            if i.accnum == acc_number:
##                i.withdraw(withdraw_amt)
##                break
##    elif choice == 3:
##        acc_number = int(input("Enter the account number: "))
##        for i in accounts:
##            if i.accnum == acc_number:
##                i.display()
##    elif choice == 4:
##        break
##    
##    else:
##        print("Invalid Input")

##class Applicant:
##    def __init__ (self, ANo,name, Agg, grade):
##        self.__ANo = ANo
##        self.__name = name
##        self.__Agg = Agg
##        self.__grade = grade
##    def __grade_me(self):
##        if self.__Agg >=80:
##            self.__grade = 'A'
##        elif 65<= self.__Agg <80:
##            self.__grade = 'B'
##        elif 50<= self.__Agg < 65:
##            self.__grade = 'C'
##        else:
##            self.__grade = 'D'
##    def ENTER(self):
##        self.__ANo = int(input("Enter the admission number: "))
##        self.__name = input("Enter the student name: ")
##        self.__Agg = int(input("Enter the aggregate score: "))
##        self.__grade_me()
##    def RESULT(self):
##        print("Adm Number: ", self.__ANo)
##        print("Name: ", self.__name)
##        print("Aggregate Score: ", self.__Agg)
##        print("Grade: ", self.__grade)
##
##student = []
##while True:
##    print("1. Enter Student Details")
##    print("2. Display Student Details")
##    print("3. Exit")
##    choice = int(input("Enter the choice: "))
##
##    if choice == 1:
##        st = Applicant(0,"",0,"")
##        st.ENTER()
##        student.append(st)
##
##    elif choice == 2:
##        Add_num = int(input("Enter the admission number: "))
##        for i in student:
##            i.RESULT()
##            break
##    elif choice == 3:
##        break
##    else:
##        print("Invalid choice.")


##class Batsmen:
##    def __init__(self, firstName, lastName, runs, fours, sixes):
##        self.firstName = firstName
##        self.lastName = lastName
##        self.runs = runs
##        self.fours = fours
##        self.sixes = sixes
##    def initialize(self):
##        self.firstName = input("Enter the first name: ")
##        self.lastName = input("Enter the last name: ")
##        self.runs = int(input("Enter the number of runs: "))
##        self.fours = int(input("Enter the number of fours: "))
##        self.sixes = int(input("Enter the number of sixes: "))
##        print("Player has been entered")
##    def update(self, newRuns):
##        self.runs = self.runs + newRuns
##    def display(self):
##        print("Name: ", self.firstName," ", self.lastName)
##        print("Runs: ", self.runs)
##        print("Fours: ", self.fours)
##        print("Sixes: ", self.sixes)
##        
##players = []
##while True:
##    print("Enter 1 to initialize")
##    print("Enter 2 to update runs")
##    print("Enter 3 to display")
##    print("Enter 4 to exit ")
##    choice = int(input("Enter your choice: "))
##
##    if choice == 1:
##        player = Batsmen("", "", 0, 0, 0)
##        player.initialize()
##        players.append(player)
##        
##    elif choice == 2:
##        name = input("Enter the player first name: ")
##        runs = int(input("Enter the new runs: "))
##        for i in players:
##            if i.firstName == name:
##                i.update(runs)
##                break
##    elif choice == 3:
##        name = input("Enter the player first name: ")
##        for i in players:
##            if i.firstName == name:
##                i.display()
##                break
##    elif choice == 4:
##        break
##    else:
##        print("Invalid Choice")

##class Ticket:
##    count =0
##    num = 0
##    money = 0
##        
##    @staticmethod
##    def initialize():
##        Ticket.count = 0
##        Ticket.num= 0
##        Ticket.money = 0
##
##    @staticmethod
##    def visit():
##        Ticket.num = Ticket.num + 1
##        
##    @staticmethod
##    def sold():
##        Ticket.num = Ticket.num + 1
##        Ticket.money = Ticket.money + 2.50
##        Ticket.count += 1
##
##    @staticmethod
##    def display():
##        print("People visited: ", Ticket.num)
##        print("Ticket total: ", Ticket.money)
##        print("Tickets sold: ", Ticket.count)
##        print(" ")
##
##while True:
##    print("Enter 1 if someone visited ")
##    print("Enter 2 if someone purchased ")
##    print("Enter 3 to display")
##    print("Enter 4 to exit ")
##    choice = int(input("Enter your choice: "))
##
##    if choice == 1:
##        Ticket.visit()
##
##    elif choice == 2:
##        Ticket.sold()
##
##    elif choice == 3:
##        Ticket.display()
##            
##    elif choice == 4:
##        break
##
##    else:
##        print("INVALID!")

import random
class admission:
    l=[]
    def __init__(self):
        self.__AD_NO = 0
        self.__NAME = ""
        self.__CLASS = ""
        self.__FEES = 0
    def Read_Data(self):
        AD_NO = random.randint(10,15)
        flat =0
        for i in admission.l:
            if i == AD_NO:
                flat =1
        if flat == 0:
            self.__AD_NO = AD_NO
            self.__NAME = input("Enter your name: ")
            self.__CLASS = input("Enter your class: ")
            self.__FEES =int(input("Enter your fees: "))
            admission.l.append(self.__AD_NO)
        else:
            print("ADmission Number already exists")
            return 2

    def display(self):
        print("Name: ", self.__NAME)
        print("Class: ", self.__CLASS)
        print("Fees: ", self.__FEES)
        print("Admission Number: ", self.__AD_NO)

    def Admission(self):
        return self.__AD_NO

    @staticmethod
    def Draw_Nos():
        return random.randint(10,15)
l1 = []
choice =0
while choice<=3:
    print("Enter 1 to initialize ")
    print("Enter 2 to diplay ")
    print("Enter 3 to exit")
    choice = int(input("Enter your choice: "))

    if choice ==1:
        ob1 = admission()
        
        if ob1.Read_Data()!=2:
            l1.append(ob1)

    elif choice ==2:
        for i1 in range(2):
            i = admission.Draw_Nos()
            for j in l1:
                if j.Admission()==i:
                    j.display()

    elif choice ==3:
        for i in l1:
            i.display()
            
            

        
