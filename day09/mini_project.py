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
        return self.by_number.get(account_number)

    def list_all(self):
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
        all_accounts = list(self.by_number.values())
        sorted_accs = sorted(all_accounts, key=lambda a: a.balance, reverse=True)
        return sorted_accs[:n]

    def find_by_number(self, account_number):
        keys = sorted(self.by_number.keys())
        idx = binary_search(keys, account_number)
        if idx == -1:
            return None
        return self.by_number[keys[idx]]

    def total_transactions(self, account_number):
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


    def build_branch_tree(self, branch_definitions):
        """
        Build a tree of branches from a nested dict structure.
        Each branch: {'name': str, 'accounts': [acc_numbers], 'children': [...]}
        Returns a Branch object (root).
        """
        def _build(defn):
            branch = Branch(defn['name'])
            for acc_num in defn.get('accounts', []):
                acc = self.find(acc_num)
                if acc is not None:
                    branch.add_account(acc)
            for child_def in defn.get('children', []):
                child = _build(child_def)
                branch.add_child(child)
            return branch
        return _build(branch_definitions)

    def add_transfer(self, from_acc, to_acc, amount):
        """Record a transfer from one account to another (directed edge)."""
        if not hasattr(self, '_transfers'):
            self._transfers = {}   
        self._transfers.setdefault(from_acc, []).append((to_acc, amount))

    def transfers_from(self, account_number):
        """Return list of (to_account, amount) for transfers out of account."""
        return self._transfers.get(account_number, [])

    def bfs_transfers(self, start_account):
        """
        BFS over the transfers graph starting from an account.
        Returns set of reachable account numbers (including start).
        """
        if not hasattr(self, '_transfers'):
            return {start_account}   
        visited = {start_account}
        q = deque([start_account])
        while q:
            cur = q.popleft()
            for to_acc, _ in self._transfers.get(cur, []):
                if to_acc not in visited:
                    visited.add(to_acc)
                    q.append(to_acc)
        return visited

class Branch:
    def __init__(self, name):
        self.name = name
        self.accounts = []      
        self.children = []        
        self.parent = None        

    def add_account(self, account):
        self.accounts.append(account)

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def total_balance(self):
        """Recursively compute total balance of this branch and all descendants."""
        total = sum(acc.balance for acc in self.accounts)
        for child in self.children:
            total += child.total_balance()
        return total

    def print_structure(self, indent=0):
        """Print the tree hierarchy with account names and balances."""
        prefix = "  " * indent
        print(f"{prefix}Branch: {self.name} (total balance: {self.total_balance():.2f} ETB)")
        for acc in self.accounts:
            print(f"{prefix}  Account: {acc.account_number} - {acc.owner} ({acc.balance} ETB)")
        for child in self.children:
            child.print_structure(indent + 1)


if __name__ == "__main__":
    registry = AccountRegistry()

    acc1 = SavingsAccount("Almaz", "SAV-001", 1500, 0.04)
    acc2 = CurrentAccount("Dawit", "CUR-001", 800, 500)
    acc3 = SavingsAccount("Hanna", "SAV-002", 2000)
    acc4 = Account("Samuel", "ACC-001", 3000)
    acc5 = Account("Tigist", "ACC-002", 500)

    registry.add(acc1)
    registry.add(acc2)
    registry.add(acc3)
    registry.add(acc4)
    registry.add(acc5)

    acc1.deposit(300)
    acc1.withdraw(100)
    acc2.withdraw(1200)
    acc3.deposit(500)
    acc3.add_interest()

    print("--- Account Registry Demo ---")
    registry.show_all_statements()

    branch_def = {
        'name': 'Head Office',
        'accounts': ['ACC-001', 'ACC-002'],
        'children': [
            {
                'name': 'Addis Ababa Branch',
                'accounts': ['SAV-001', 'CUR-001'],
                'children': [
                    {'name': 'Bole Sub-branch', 'accounts': ['SAV-002']}
                ]
            }
        ]
    }
    root_branch = registry.build_branch_tree(branch_def)
    print("\n--- Branch Tree Structure ---")
    root_branch.print_structure()

    registry.add_transfer("SAV-001", "CUR-001", 200)
    registry.add_transfer("CUR-001", "ACC-001", 150)
    registry.add_transfer("ACC-001", "SAV-002", 300)
    registry.add_transfer("SAV-002", "ACC-002", 100)

    print("\n--- Transfers Graph ---")
    for acc_num in registry.by_number:
        transfers = registry.transfers_from(acc_num)
        if transfers:
            print(f"{acc_num} -> {transfers}")

    print("\nBFS reachable from SAV-001:", registry.bfs_transfers("SAV-001"))
    print("BFS reachable from ACC-002:", registry.bfs_transfers("ACC-002"))