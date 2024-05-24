#(Homework) Question 4
class BankAccount:
    def __init__(self, acc_number: str, acc_holder: str, balance: float = 0.0):
        self.acc_number = acc_number
        self.acc_holder = acc_holder
        self.balance = balance

    def deposit(self, amount: float):
        self.balance += amount

    def withdraw(self, amount: float):
        self.balance -= amount if amount <= self.balance else print("Insufficient funds.")

    def get_balance(self) -> float:
        return self.balance


class SavingsAccount(BankAccount):
    def __init__(self, acc_number: str, acc_holder: str, balance: float = 0.0, interest_rate: float = 0.01):
        super().__init__(acc_number, acc_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        self.balance += self.balance * self.interest_rate

    def __str__(self):
        return f"Balance: ${self.balance:.2f}, Interest Rate: {self.interest_rate * 100}%"


# Test the classes
account = BankAccount("007007", "Bashar Yaseen")
account.deposit(3000)
print(f"After deposit, balance: ${account.get_balance()}")
account.withdraw(700)
print(f"After withdrawal, balance: ${account.get_balance()}")

savings_account = SavingsAccount("008008", "Bashar Yaseen", 6000, 0.05)
savings_account.apply_interest()
print(savings_account)
