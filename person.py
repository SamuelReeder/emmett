class Person:
    
    def __init__(self, name: str, iDeposit: int) -> None:
        self.name = name
        self.savingsAccount = []
        self.savingsAccount.append(iDeposit)
        self.lifeSavings = []
        self.finalBalance = 0
        