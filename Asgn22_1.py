class Demo:
    Value = 10
    
    def __init__(self,A,B):
        self.No1 = A
        self.No2 = B

    def Fun(self):
        print("Inside Fun()")
        print("Value of instance variables using obj1:",obj1.No1, obj1.No2)
        print("Value of instance variables using obj2:",obj2.No1, obj2.No2)

    def Gun(self):
        print("Inside Gun()")
        print("Value of instance variables using obj1:",obj1.No1, obj1.No2)
        print("Value of instance variables using obj2:",obj2.No1, obj2.No2)

obj1 = Demo(11,21)
obj2 = Demo(51,101)

print("Class variable accessed:", Demo.Value)

obj1.Fun()
obj2.Fun()
obj1.Gun()
obj2.Gun()