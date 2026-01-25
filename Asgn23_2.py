from Asgn23_2Exception import InvalidWithdrawAmountError
class BankAccount:
    ROI = 10.5
    
    def __init__(self, Name, Amount):
        self.Nm = Name
        self.Amt = Amount
        
        

    def Deposit(self):
        print("Enter the Amount to Deposit:")
        DepositAmount = int(input())

        self.Amt = self.Amt + DepositAmount
    
    def Withdraw(self):
        print("Enter the Amount to Withdraw:")
        WithdrawAmount = int(input())
        try:
            if WithdrawAmount > self.Amt:
                raise InvalidWithdrawAmountError(WithdrawAmount)
            else:
                self.Amt = self.Amt - WithdrawAmount
            
        except InvalidWithdrawAmountError as invObj:
            
            print(invObj)

    def CalculateInterest(self):
        Interest = (self.Amt*BankAccount.ROI)/100
        print("Interest is:", Interest)

    def Display(self):
        print(f"{self.Nm} has a balance of {self.Amt}")

obj1 = BankAccount("Swami", 1000)
obj1.Deposit()
obj1.Withdraw()
obj1.CalculateInterest()
obj1.Display()

obj2 = BankAccount("Krish", 5000)
obj2.Deposit()
obj2.Withdraw()
obj2.CalculateInterest()
obj2.Display()

