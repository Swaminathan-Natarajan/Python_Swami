class Bookstore:
    NoOfBooks = 0
    
    def __init__(self, Name, Author):
        self.Nm = Name
        self.Auth = Author
        Bookstore.NoOfBooks = Bookstore.NoOfBooks + 1
        

    #def Accept(self):
        #print("Enter the Book Name:")
       # self.Name = input()
#
 #       print("Enter the Author Name:")
  #      self.Author = input()
        
    
    def Display(self):
        print(f"{self.Nm} by {self.Auth}. No Of Books: {Bookstore.NoOfBooks}")

obj1 = Bookstore("Linux System Programming", "Robert Love")
#obj1.Accept()
obj1.Display()

obj2 = Bookstore("C Programming" ,"Dennis Ritchie")
#obj2.Accept()
obj2.Display()
