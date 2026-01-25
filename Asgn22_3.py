class Arithmetic:
    PI = 3.14
    
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0
        

    def Accept(self):
        print("Enter the Value1:")
        self.Value1 = int(input())

        print("Enter the Value2:")
        self.Value2 = int(input())
        

    def Addition(self):
        Add = self.Value1 + self.Value2
        return Add

    def Substraction(self):
        Sub = self.Value1 - self.Value2
        return Sub

    def Multiplication(self):
        Mul = self.Value1 * self.Value2
        return Mul

    def Division(self):
        try:
            Div = self.Value1 / self.Value2
            return Div
        except ZeroDivisionError as ZD:
            print(ZD)
    
    def Display(self,Add, Sub, Mul, Div):
        print("Addition is:", Add )
        print("Substraction is:",Sub)
        print("Multiplication is:", Mul)
        print("Division is:", Div)

obj1 = Arithmetic()
obj1.Accept()
Add = obj1.Addition()
Sub = obj1.Substraction()
Mul = obj1.Multiplication()
Div = obj1.Division()
obj1.Display(Add, Sub, Mul, Div)

obj2 = Arithmetic()
obj2.Accept()
Add = obj2.Addition()
Sub = obj2.Substraction()
Mul = obj2.Multiplication()
Div = obj2.Division()
obj2.Display(Add, Sub, Mul, Div)
