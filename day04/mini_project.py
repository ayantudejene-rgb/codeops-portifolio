class Account:
    """A bank account with owner, account number, and private balance."""
    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self._balance = balance   
    @property
    def balance(self):
        """Read-only balance property."""
        return self._balance
    def deposit(self, amount):
        """Add a positive amount to the balance."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount
    def withdraw(self, amount):
        """Subtract a positive amount if sufficient funds exist."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self._balance:
            raise ValueError(f"Insufficient funds. Balance: {self._balance} ETB")
        self._balance -= amount
    def statement(self):
        """Print the account summary."""
        print(f"Account: {self.account_number}")
        print(f"Owner:   {self.owner}")
        print(f"Balance: {self._balance} ETB")
if __name__ == "__main__":
    almaz = Account("Almaz Bekele", "001", 1500)
    dawit = Account("Dawit Tesfaye", "002", 800)
    almaz.deposit(500)
    almaz.withdraw(200)
    almaz.statement()
    dawit.deposit(100)
    dawit.statement()
