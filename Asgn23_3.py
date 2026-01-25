
class Numbers:
    
    def __init__(self):
        self.Value = 0
                

    def Accept(self):
        print("Enter the number:")
        self.Value = int(input())


    def ChkPrime(self):
        for i in range(2,self.Value):
            if self.Value % i == 0:
                return False
            else:
                return True
    
    def ChkPerfect(self):
        sum = 0
        for i in range(1,self.Value):
            if self.Value % i == 0:                
                sum = sum + i
        return sum

    def Factorial(self):
        fact = 1
        for i in range(1,self.Value+1):
            fact = fact * i

        return fact

    def SumFactors(self):
        sum = 0
        for i in range(1,self.Value):
            if self.Value % i == 0:                
                sum = sum + i
        return sum

obj1 = Numbers()
obj1.Accept()
Ret = obj1.ChkPrime()
if Ret == True:
    print("Entered number is Prime number:", obj1.Value)
else:
    print("Entered number is Not Prime number:", obj1.Value)
Ret1 = obj1.ChkPerfect()
if Ret1 == obj1.Value:
    print("Entered number is Perfect number:", obj1.Value)
else:
    print("Entered number is Not Perfect number:", obj1.Value)
Ret2 = obj1.Factorial()
print("Factorial of the given number is:", Ret2)

Ret3 = obj1.SumFactors()
print("Sum of Factors is:", Ret3)

