class InvalidWithdrawAmountError(Exception):
    
    def __init__(self, Amount, msg="Withdraw Amount cannot exceed Available balance"):
        self.Amt = Amount
        self.msg = msg
        super().__init__(f"{msg} Given: {Amount}")
        


