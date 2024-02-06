class Account:
    def __init__(self, owner = "", balance = 0):
        self.owner = owner
        self.balance = balance
    def Deposit(self, aai):
        self.balance += aai
    def Withdraw(self, aai):
        if self.balance < aai:
            print(f"{self.owner}, withdraw is not possible.")
        else:
            self.balance -= aai

account = Account("Alice", 50000)
print(account.balance)

account.Deposit(10000)
print(account.balance)

account.Withdraw(100000) 
account.Withdraw(5000)
print(account.balance)

