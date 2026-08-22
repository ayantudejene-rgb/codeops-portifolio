from abc import ABC, abstractmethod 
class Account:
    """Base account class with owner, number, and private balance."""
    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self._balance = balance
    @property
    def balance(self):
        return self._balance
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self._balance:
            raise ValueError(f"Insufficient funds. Balance: {self._balance} ETB")
        self._balance -= amount
    def statement(self):
        print(f"Account: {self.account_number} | Owner: {self.owner} | Balance: {self._balance} ETB")
class SavingsAccount(Account):
    def __init__(self, owner, account_number, balance=0, rate=0.05):
        super().__init__(owner, account_number, balance)   # reuse parent init
        self.rate = rate
    def add_interest(self):
        interest = self.balance * self.rate
        self.deposit(interest)   # reuse parent deposit
        print(f"Added interest: {interest:.2f} ETB")
    def statement(self):
        print(f"[Savings] {self.account_number} | {self.owner} | {self.balance} ETB (rate: {self.rate*100:.0f}%)")
class CurrentAccount(Account):
    def __init__(self, owner, account_number, balance=0, overdraft=1000):
        super().__init__(owner, account_number, balance)
        self.overdraft = overdraft
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance + self.overdraft:
            raise ValueError(f"Overdraft limit exceeded. Available: {self.balance + self.overdraft} ETB")
        self._balance -= amount 
    def statement(self):
        print(f"[Current] {self.account_number} | {self.owner} | {self.balance} ETB (overdraft: {self.overdraft} ETB)")
if __name__ == "__main__":
    accounts = [
        Account("Hanna", "001", 1500),
        SavingsAccount("Almaz", "002", 1500, 0.04),
        CurrentAccount("Dawit", "003", 800, 500),
    ]

    print("Account Statements (Polymorphic) ")
    for acc in accounts:
        acc.statement()       
    print("\nOperations")
    # Operate on each account
    accounts[0].deposit(200)     
    accounts[1].add_interest()   
    accounts[2].withdraw(1000)    
    print("\nAfter Operations")
    for acc in accounts:
        acc.statement()
    try:
        accounts[2].withdraw(2000)  
    except ValueError as e:
        print(f"\nError: {e}")