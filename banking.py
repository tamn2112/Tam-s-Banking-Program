class Banking:
    def __init__(self, total_balance):
        self._total_balance = total_balance
    
    def deposit(self, amount: float):
        if amount > 0:
            self._total_balance += amount
        return self._total_balance
            
    def withdraw(self, amount: float):
        if self._total_balance >= amount:
            self._total_balance -= amount
            return self._total_balance
        else: return 0
    
    def display(self):
        return f"Your total balance is: {self._total_balance}"

    @property
    def get_total_balance(self):
        return self._total_balance
    
    def verify_sufficient_fund(self, withdraw_amount):
        return self._total_balance >= withdraw_amount
    
    def verify_deposit_amount(self, deposit_amount):
        return deposit_amount > 0

