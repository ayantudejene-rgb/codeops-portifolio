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
        if not self._history:
            raise ValueError("No transactions to undo.")
        action, amount = self._history.pop()
        if action == "deposit":
            self._balance -= amount
        else:  
            self._balance += amount
        return f"Undid {action} of {amount} ETB"
    def get_history(self):
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

def binary_search(sorted_list, target):
    """Return index of target in sorted list, or -1."""
    lo, hi = 0, len(sorted_list) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
class AccountRegistry:
    def __init__(self):
        self.by_number = {}      
        self.order = []          

    def add(self, account):
        if account.account_number in self.by_number:
            raise ValueError(f"Account {account.account_number} already exists.")
        self.by_number[account.account_number] = account
        self.order.append(account.account_number)
    def find(self, account_number):
        """O(1) dict lookup."""
        return self.by_number.get(account_number)
    def list_all(self):
        """Return accounts in insertion order."""
        return [self.by_number[num] for num in self.order]
    def undo_last(self, account_number):
        acc = self.find(account_number)
        if acc is None:
            raise ValueError(f"Account {account_number} not found.")
        return acc.undo_last()
    def show_all_statements(self):
        for acc in self.list_all():
            acc.statement()
    def top_by_balance(self, n=5):
        """Return the top n accounts by balance (descending)."""
        all_accounts = list(self.by_number.values())
        sorted_accs = sorted(all_accounts, key=lambda a: a.balance, reverse=True)
        return sorted_accs[:n]
    def find_by_number(self, account_number):
        """Use binary search over sorted account numbers to find an account.
           Returns the Account or None if not found.
        """
        keys = sorted(self.by_number.keys())   
        idx = binary_search(keys, account_number)
        if idx == -1:
            return None
        return self.by_number[keys[idx]]
    def total_transactions(self, account_number):
        """Recursively sum all transaction amounts for an account.
           Returns the sum (deposits positive, withdrawals negative).
        """
        acc = self.find(account_number)
        if acc is None:
            raise ValueError(f"Account {account_number} not found.")
        def _sum_history(history, index=0):
            if index >= len(history):
                return 0
            action, amount = history[index]
            sign = 1 if action == "deposit" else -1
            return sign * amount + _sum_history(history, index + 1)
        return _sum_history(acc.get_history())
if __name__ == "__main__":
    registry = AccountRegistry()
    acc1 = SavingsAccount("Almaz", "SAV-001", 1500, 0.04)
    acc2 = CurrentAccount("Dawit", "CUR-001", 800, 500)
    acc3 = SavingsAccount("Hanna", "SAV-002", 2000)
    acc4 = Account("Samuel", "ACC-001", 3000)
    registry.add(acc1)
    registry.add(acc2)
    registry.add(acc3)
    registry.add(acc4)
    acc1.deposit(300)
    acc1.withdraw(100)
    acc2.withdraw(1200)   
    acc3.deposit(500)
    acc3.add_interest()   
    print("--- All Accounts ---")
    registry.show_all_statements()
    print("\n--- Top 3 by Balance ---")
    for acc in registry.top_by_balance(3):
        print(f"{acc.owner} ({acc.account_number}): {acc.balance} ETB")
    print("\n--- Binary search find ---")
    found = registry.find_by_number("CUR-001")
    if found:
        print(f"Found: {found.owner} ({found.account_number})")
    else:
        print("Not found")
    not_found = registry.find_by_number("XXX-001")
    print(f"Search for XXX-001: {'Not found' if not_found is None else 'Found'}")
    print("\n--- Recursive transaction total ---")
    total1 = registry.total_transactions("SAV-001")
    print(f"Total transaction sum for SAV-001: {total1} ETB")
    total2 = registry.total_transactions("SAV-002")
    print(f"Total transaction sum for SAV-002: {total2} ETB")