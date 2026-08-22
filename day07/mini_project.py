from collections import deque
import time
class Account:
    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self._balance = balance
        self._history = []   

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount
        self._history.append(("deposit", amount))

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self._balance:
            raise ValueError(f"Insufficient funds. Balance: {self._balance} ETB")
        self._balance -= amount
        self._history.append(("withdraw", amount))

    def undo_last(self):
        """Undo the most recent transaction."""
        if not self._history:
            raise ValueError("No transactions to undo.")
        action, amount = self._history.pop()
        if action == "deposit":
            self._balance -= amount 
        elif action == "withdraw":
            self._balance += amount  
        return f"Undid {action} of {amount} ETB"

    def get_history(self):
        """Return a copy of the transaction history (most recent last)."""
        return self._history.copy()

    def statement(self):
        print(f"Account: {self.account_number} | {self.owner} | Balance: {self._balance} ETB")

class SavingsAccount(Account):
    def __init__(self, owner, account_number, balance=0, rate=0.05):
        super().__init__(owner, account_number, balance)
        self.rate = rate

    def add_interest(self):
        interest = self.balance * self.rate
        self.deposit(interest)   
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
        self._history.append(("withdraw", amount))

    def statement(self):
        print(f"[Current] {self.account_number} | {self.owner} | {self.balance} ETB (overdraft: {self.overdraft} ETB)")

class AccountRegistry:
    """Stores accounts in a dict for O(1) lookup and a list for insertion order."""
    def __init__(self):
        self.by_number = {}  
        self.order = []         

    def add(self, account):
        """Add an account (O(1))."""
        if account.account_number in self.by_number:
            raise ValueError(f"Account {account.account_number} already exists.")
        self.by_number[account.account_number] = account
        self.order.append(account.account_number)

    def find(self, account_number):
        """Look up an account by number (O(1))."""
        return self.by_number.get(account_number)

    def list_all(self):
        """Return accounts in insertion order."""
        return [self.by_number[num] for num in self.order]

    def undo_last(self, account_number):
        """Undo the last transaction for a given account."""
        acc = self.find(account_number)
        if acc is None:
            raise ValueError(f"Account {account_number} not found.")
        return acc.undo_last()

    def show_all_statements(self):
        """Print statement for each account in insertion order."""
        for acc in self.list_all():
            acc.statement()
if __name__ == "__main__":
    registry = AccountRegistry()

    acc1 = SavingsAccount("Almaz", "SAV-001", 1500, 0.04)
    acc2 = CurrentAccount("Dawit", "CUR-001", 800, 500)
    acc3 = SavingsAccount("Hanna", "SAV-002", 2000)
    registry.add(acc1)
    registry.add(acc2)
    registry.add(acc3)
    print("--- Transactions ---")
    acc1.deposit(300)
    acc1.withdraw(100)
    acc2.withdraw(1200)      
    acc3.deposit(500)
    acc3.add_interest()
    print("\n--- All Accounts ---")
    registry.show_all_statements()
    print(f"\nHistory for {acc1.account_number}: {acc1.get_history()}")
    print("\nUndo acc1's last transaction:")
    print(registry.undo_last("SAV-001"))
    acc1.statement()
    print("\nUndo another:")
    print(registry.undo_last("SAV-001"))
    acc1.statement()
    print("\n--- O(1) lookup test ---")
    found = registry.find("CUR-001")
    if found:
        print(f"Found: {found.owner} ({found.account_number})")
    print("\n Listing all in insertion order")
    for acc in registry.list_all():
        print(acc.account_number, acc.owner)