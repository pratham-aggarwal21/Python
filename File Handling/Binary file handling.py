import pickle

class Book:
    def __init__(self, book_number = 0, book_name=" ", author = " ",
                 publisher = " ", price = 0, num_of_copies = 0 , issued = 0):
        self.book_number = book_number
        self.book_name = book_name
        self.author  = author
        self.publisher = publisher
        self.price = price
        self.num_of_copies = num_of_copies
        self.issued = issued
    def issue(self):
        self.issued = self.issued + 1
    def display(self):
        print(self.book_number, self.book_name, self.author, self.publisher, self.price,
              self.price, self.num_of_copies, self.issued)
    def rno(self):
        return self.book_number

ch = 0
l =[]

while ch<=5:
    print("Press 1 for insert")
    print("Press 2 for search")
    print("Press 3 for display")
    print("press 4 for issue: ")
    print("press 5 for delete: ")
    ch = int(input("Enter your choice:"))
    if ch==1:
        number = int(input("Enter the book number: "))
        name = input("Enter the book name: ")
        publisher = input("Enter the publisher: ")
        price = int(input("Enter the price: "))
        num1= int(input("Enter the number of copies: "))
        ob1 = Book(number, name, publisher, price, num1, 0)
        file1 = open("book.log","ab")
        pickle.dump(ob1,file1)
        file1.close()
    elif ch==2:
        number = int(input("Enter the book number: "))
        file1 = open("book.log","rb")
        try:
            while True:
                ob1 = pickle.load(file1)
                ob1.rno()
                if ob1.rno()==number:
                    ob1.display()
        except EOFError:
            file1.close()    
            
    elif ch==3:        
        file1 = open("book.log","rb")
        try:
            while True:
                ob1 = pickle.load(file1)
                ob1.display()  ## Calling the display func
        except EOFError:
            file1.close()

    elif ch==4:
        number = int(input("Enter the book number: "))
        file1 = open("book.log","rb")
        file2 =open("temp.log","wb")
        try:
            while True:
                ob1 = pickle.load(file1)
                ob1.rno()
                if ob1.rno()==number:
                    ob1.issue()
                pickle.dump(ob1,file2)
        except EOFError:
            file1.close()
            file2.close()
        file1 = open("book.log", "wb")
        file2 = open("temp.log", "rb")
        try:
            while True:
                ob1 = pickle.load(file2)
                pickle.dump(ob1,file1)
        except EOFError:
            file1.close()
            file2.close()

    elif ch==5:
        number = int(input("Enter the book number: "))
        file1 = open("book.log","rb")
        file2 =open("temp.log","wb")
        try:
            while True:
                ob1 = pickle.load(file1)
                ob1.rno()
                if ob1.rno()!=number:
                    pickle.dump(ob1,file2)
        except EOFError:
            file1.close()
            file2.close()
        file1 = open("book.log", "wb")
        file2 = open("temp.log", "rb")
        try:
            while True:
                ob1 = pickle.load(file2)
                pickle.dump(ob1,file1)
        except EOFError:
            file1.close()
            file2.close()
