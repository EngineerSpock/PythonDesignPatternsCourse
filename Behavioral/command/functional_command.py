class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

def deposit(account, amount):
    account.balance += amount

def withdraw(account, amount):
    if account.balance >= amount:
        account.balance -= amount


# if all you want to do is group actions together...
if __name__ == '__main__':
    ba = BankAccount()
    commands = []

    commands.append(lambda a: deposit(a, 100))
    commands.append(lambda a: withdraw(a, 50))

    for c in commands:
        c(ba)

    print(ba.balance)