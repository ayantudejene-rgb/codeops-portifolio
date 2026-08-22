class BankConfig:
    """Singleton holding shared bank settings."""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            # Set default values
            cls._instance.interest_rate = 0.05      # 5%
            cls._instance.overdraft_limit = 1000    # ETB
        return cls._instance

class Account:
    """Base account with balance, deposit, withdraw, and observer support."""
    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self._balance = balance
        self._observers = []   # list of observers to notify on changes

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount
        self._notify(f"Deposited {amount} ETB")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self._balance:
            raise ValueError(f"Insufficient funds. Balance: {self._balance} ETB")
        self._balance -= amount
        self._notify(f"Withdrew {amount} ETB")

    def statement(self):
        print(f"Account: {self.account_number} | Owner: {self.owner} | Balance: {self._balance} ETB")

    def subscribe(self, observer):
        """Add an observer that will be notified on every transaction."""
        self._observers.append(observer)

    def _notify(self, event):
        """Notify all observers about a transaction event."""
        for obs in self._observers:
            obs.update(self, event)

class SMSAlert:
    """Sends an SMS alert on transactions."""
    def update(self, account, event):
        print(f"[SMS] Alert for {account.owner} ({account.account_number}): {event}")

class AuditLog:
    """Logs transactions to a file or console."""
    def update(self, account, event):
        print(f"[Audit] {account.account_number} – {event}")

class SavingsAccount(Account):
    def __init__(self, owner, account_number, balance=0, rate=None):
        config = BankConfig()
        if rate is None:
            rate = config.interest_rate
        super().__init__(owner, account_number, balance)
        self.rate = rate

    def add_interest(self):
        interest = self.balance * self.rate
        self.deposit(interest)
        print(f"Added interest: {interest:.2f} ETB")

    def statement(self):
        print(f"[Savings] {self.account_number} | {self.owner} | {self.balance} ETB (rate: {self.rate*100:.0f}%)")

class CurrentAccount(Account):
    def __init__(self, owner, account_number, balance=0, overdraft=None):
        config = BankConfig()
        if overdraft is None:
            overdraft = config.overdraft_limit
        super().__init__(owner, account_number, balance)
        self.overdraft = overdraft

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance + self.overdraft:
            raise ValueError(f"Overdraft limit exceeded. Available: {self.balance + self.overdraft} ETB")
        self._balance -= amount
        self._notify(f"Withdrew {amount} ETB (overdraft allowed)")

    def statement(self):
        print(f"[Current] {self.account_number} | {self.owner} | {self.balance} ETB (overdraft: {self.overdraft} ETB)")

# -------------------- Factory --------------------
class AccountFactory:
    """Creates accounts by type – decouples client from concrete classes."""
    @staticmethod
    def create(kind, owner, account_number, balance=0):
        if kind == "savings":
            return SavingsAccount(owner, account_number, balance)
        elif kind == "current":
            return CurrentAccount(owner, account_number, balance)
        else:
            raise ValueError(f"Unknown account type: {kind}")

# -------------------- Demo (polymorphic + patterns) --------------------
if __name__ == "__main__":
    config1 = BankConfig()
    config2 = BankConfig()
    print(f"BankConfig is Singleton: {config1 is config2}")

    acc1 = AccountFactory.create("savings", "Almaz", "SAV-001", 1500)
    acc2 = AccountFactory.create("current", "Dawit", "CUR-001", 800)
    acc3 = AccountFactory.create("savings", "Hanna", "SAV-002", 2000)

    sms = SMSAlert()
    audit = AuditLog()
    acc1.subscribe(sms)
    acc1.subscribe(audit)
    acc2.subscribe(sms)       

    print("\n--- Operations ---")
    acc1.deposit(300)         
    acc1.withdraw(100)        
    acc2.withdraw(1200)       
    acc3.add_interest()      

    print("\n--- Statements ---")
    accounts = [acc1, acc2, acc3]
    for a in accounts:
        a.statement()