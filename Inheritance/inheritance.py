##class publication:
##    def __init__(self,title, price):
##        self.title = title
##        self.price = price
##
##    def getdata(self):
##        self.title = input("Enter the title: ")
##        self.price = int(input("Enter the price: "))
##
##    def display(self):
##        print("Title: ", self.title)
##        print("Price: ", self.price)
##
##class book(publication):
##    def __init__(self, title, price, page_count):
##        publication.__init__(self, title, price)
##        self.page_count = page_count
##
##    def getdata(self):
##        print("For book")
##        super(book, self).getdata()
##        self.page_count = int(input("Enter the page count: "))
##
##    def display(self):
##        super(book, self).display()
##        print("Page count: ", self.page_count)
##
##class tape(publication):
##    def __init__(self, title, price, playing_time):
##        publication.__init__(self, title, price)
##        self.playing_time = playing_time
##
##    def getdata(self):
##        print("For tape")
##        super(tape, self).getdata()
##        self.playing_time = int(input("Enter the playing time: "))
##
##    def display(self):
##        super(tape, self).display()
##        print("Playing time: ", self.playing_time)
##
##l1 = []
##l2=[]
##while True:
##    print("Enter 1 to input data of book")
##    print("Enter 2 to display data of book")
##    print("Enter 3 to input data of tape")
##    print("Enter 4 to display data of tape")
##    print("Enter 5 exit")
##    ch = int(input("Enter your choice: "))
##
##    if ch == 1:
##        ob1 = book("", 0,0)
##        ob1.getdata()
##        l1.append(ob1)
##
##    elif ch == 2:
##        for i in l1:
##            i.display()
##
##    elif ch == 3:
##        ob2 = tape("", 0,0)
##        ob2.getdata()
##        l2.append(ob2)
##
##    elif ch == 4:
##        for i in l2:
##            i.display()
##
##    elif ch ==5:
##        break
##
##    else:
##        print("wrong input")


##class Account:
##    def __init__(self, name, num, op_balance):
##        self.name= name
##        self.num = num
##        self.op_balance = op_balance
##
##    def initialize(self):
##        self.name = input("Enter the name: ")
##        self.num = int(input("Enter the acc num: "))
##        self.op_balance = int(input("Enter the opening balance: "))
##
##    def display(self):
##        print("Name: ", self.name)
##        print("Account Num: ", self.num)
##
##        
##class Current(Account):
##    def __init__ (self, name, num, op_balance,amt_update, ci, n, t,service_charge):
##        Account.__init__(self, name, num, op_balance)
##        self.amt_update= amt_update
##        self.ci = ci
##        self.n = n
##        self.t = t
##        self.service_charge= service_charge
##
##    def initialize(self):
##        super(Current, self).initialize()
##        print("account created")
##        
##    def update(self):
##        self.amt_update = int(input("Enter the amount to withdraw: "))
##        self.op_balance = self.op_balance - self.amt_update
##        self.n = int(input("Enter the number of times interest applied: "))
##        self.t = int(input("Enter the time elapsed: "))
##        self.ci = self.op_balance * pow((1+(5/self.n)), self.n * self.t)
##        print("Account updated")
##
##    def check(self):
##        if self.op_balance<= 1000:
##            self.service_charge =  25
##        else:
##            self.service_charge = 0 
##
##    def display(self):
##        Current.check(self)
##        super(Current, self).display()
##        print("Updated amount: ", self.op_balance)
##        print("Compound interest: ",self.ci)
##        print("Service Charge: ", self.service_charge)
##
##    def accnum(self):
##        return self.num
##
##class Savings(Account):
##    def __init__(self, name, num, op_balance, upd_amt):
##        Account.__init__(self, name, num, op_balance)
##        self.upd_amt = upd_amt
##
##    def initialize(self):
##        super(Savings, self).initialize()
##        print("account created")
##        
##    def update(self):
##        self.upd_amt = int(input("Enter the amount to withdraw: "))
##        self.op_balance = self.op_balance - self.upd_amt
##        print("Account updated")
##
##    def display(self):
##        super(Savings, self).display()
##        print("updated amount: ", self.upd_amt)
##
##    def accnum(self):
##        return self.num
##    
##
##l1 = []
##l2 = []
##while True:
##    print("Enter 1 to open a current account")
##    print("Enter 2 to update data of current account")
##    print("Enter 3 to open a savings account")
##    print("Enter 4 to update data of savings account")
##    print("Enter 5 to display details of current account")
##    print("Enter 6 to display details of savings account")
##    print("Enter 7 exit")
##    ch = int(input("Enter your choice: "))
##
##    if ch == 1:
##        ob1 = Current("",0,0,0,0.0,0,0,0 )
##        ob1.initialize()
##        l1.append(ob1)
##
##    elif ch==2:
##        num = int(input("Enter the acc num: "))
##        for i in l1:
##            if i.accnum() == num:
##                i.update()
##
##    elif ch == 3:
##        ob2 = Savings("", 0,0,0)
##        ob2.initialize()
##        l2.append(ob2)
##
##    elif ch==4:
##        num = int(input("Enter the acc num: "))
##        for i in l2:
##            if i.accnum == num:
##                i.update()
##    elif ch==5:
##        num = int(input("Enter the acc num: "))
##        for i in l1:
##            if i.accnum() == num:
##                i.display()
##
##    elif ch==6:
##        num = int(input("Enter the acc num: "))
##        for i in l2:
##            if i.accnum() == num:
##                i.display()
##            
##    elif ch==7:
##        break
##
##    else:
##        print("invalid choice")
    
##class person:
##    def __init__(self, name, phone):
##        self.name= name
##        self.phone = phone
##
##    def initialize(self):
##        self.name = input("Enter the name:")
##        self.phone = int(input("Enter the phone: "))
##    def display(self):
##        print("Name: ", self.name)
##        print("Phone: ", self.phone)
##
##    def __del__(self):
##        print("Destructor called")
##
##class spouse(person):
##    def __init__(self, name, phone, spouseName):
##        person.__init__(self, name, phone)
##        self.spouseName = spouseName
##
##    def initialize(self):
##        super(spouse, self).initialize()
##        self.spouseName = input("Enter the spouse name: ")
##    def display(self):
##        super(spouse, self).display()
##        print("Spouse Name: ", self.spouseName)
##
##
##ob2 = person("", 0)
##ob1 = spouse("",0,"")
##ob1.initialize()
##ob1.display()
##
##del ob2
##            


##class person:
##    def __init__(self, name, phone):
##        self.name= name
##        self.phone = phone
##
##    def initialize(self):
##        self.name = input("Enter the name:")
##        self.phone = int(input("Enter the phone: "))
##    def display(self):
##        print("Name: ", self.name)
##        print("Phone: ", self.phone)
##
##class Clerk(person):
##    def __init__(self, name, phone, qual, exp):
##        person.__init__(self, name, phone)
##        self.qual = qual
##        self.exp = exp
##
##    def initialize(self):
##        print("Clerk")
##        super(Clerk, self).initialize()
##        self.qual = input("Enter the qualification of clerk: ")
##        self.exp = int(input("Enter the experience of clerk: "))
##
##    def display(self):
##        super(Clerk, self).display()
##        print("Clerk")
##        print("Qualification: ", self.qual)
##        print("Experience: ", self.exp)
##
##class Officer(person):
##    def __init__(self, name, phone, qual, exp):
##        person.__init__(self, name, phone)
##        self.qual = qual
##        self.exp = exp
##
##    def initialize(self):
##        print("Officer")
##        super(Officer, self).initialize()
##        self.qual = input("Enter the qualification for officer: ")
##        self.exp = int(input("Enter the experience of the officer: "))
##
##    def display(self):
##        super(Officer, self).display()
##        print("Officer")
##        print("Qualification: ", self.qual)
##        print("Experience: ", self.exp)
##
##
##l1 = []
##l2=[]
##while True:
##    print("Enter 1 to input data of clerk")
##    print("Enter 2 to input data of officer")
##    print("Enter 3 to print  data of clerk")
##    print("Enter 4 to print data of officer")
##    print("Enter 5 to exit")
##    ch = int(input("Enter your choice: "))
##
##    if ch==1:
##        ob1 = Clerk("", 0,"",0)
##        ob1.initialize()
##        l1.append(ob1)
##
##    elif ch==2:
##        ob2 = Officer("",0,"",0)
##        ob2.initialize()
##        l2.append(ob2)
##
##    elif ch ==3:
##        for i in l1:
##            i.display()
##
##    elif ch==4:
##        for i in l2:
##            i.display()
##    elif ch==5:
##        break
##    else:
##        print("Invalid choie")


##class Student:
##    def __init__(self, name, age):
##        self.name = name
##        self.age = age
##
##    def readData(self):
##        self.name = input("Enter the name: ")
##        self.age = int(input("Enter the age: "))
##
##    def display(self):
##        print("Name: ", self.name)
##        print("Age: ", self.age)
##
##class primary(Student):
##    def __init__(self, name, age, activity):
##        Student.__init__(self, name, age)
##        self.activity = activity
##
##    def readPrimary(self):
##        super(primary, self).readData()
##        self.activity = int(input("Enter the activity hrs:" ))
##    def displayPrimary(self):
##        super(primary, self).display()
##        print("Activity hrs: ",self.activity)
##
##
##class Secondary(Student):
##    def __init__(self, name, age, lang):
##        Student.__init__(self, name, age)
##        self.lang = lang
##
##    def readSecondary(self):
##        super(Secondary, self).readData()
##        self.lang = input("Enter the language:" )
##    def displaySecondary(self):
##        super(Secondary, self).display()
##        print("Language: ",self.lang)
##
##l1 = []
##l2=[]
##while True:
##    print("Enter 1 to input data for primary student")
##    print("Enter 2 to input data for secondary student")
##    print("Enter 3 to print data for primary student")
##    print("Enter 4 to print data for secondary student")
##    print("Enter 5 to exit")
##    ch = int(input("Enter your choice: "))
##
##    if ch ==1:
##        ob1 = primary("",0,0)
##        ob1.readPrimary()
##        l1.append(ob1)
##
##    elif ch ==2:
##        ob2 = Secondary("",0,"")
##        ob2.readSecondary()
##        l2.append(ob2)
##
##    elif ch ==3:
##        for i in l1:
##            i.displayPrimary()
##    elif ch==4:
##        for i in l2:
##            i.displaySecondary()
##
##    elif ch==5:
##        break
##    else:
##        print("Invalid choice")

##class employee:
##    def __init__(self, num, add, dep,name):
##        self.num = num
##        self.add= add
##        self.dep = dep
##        self.name = name
##
##
##
##class manager(employee):
##    def __init__(self, num, add, dep, name):
##        employee.__init__(self, num, add, dep, name)
##
##    def initialize(self):
##        self.num = input("Enter the name: ")
##        self.num = int(input("Enter the employee number: "))
##        self.add = input("Enter the address: ")
##        self.dep = input("Enter the department: ")
##
##    def display(self):
##        print("Name: ",self.name)
##        print("Num: ",self.num)
##        print("Address: ",self.add)
##        print("Department: ",self.dep)
##
##l1 = []
##while True:
##    print("Enter 1 to input")
##    print("Enter 2 to display")
##    print("Enter 3 to exit")
##    ch = int(input("Enter the choice: "))
##
##    if ch==1:
##        ob1 = manager(0,"","","")
##        ob1.initialize()
##        l1.append(ob1)
##
##    elif ch==2:
##        for i in l1:
##            i.display()
##
##    elif ch==3:
##        break
##
##    else:
##        print("Invalid Input")
        
        
        
