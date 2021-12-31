class BankAccount:
    bankAccounts = []
    def __init__(self, int_rate = 0.001, balance = 0 ):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.bankAccounts.append(self)


    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(f'balance: {self.balance}')

    def yield_interest(self):
        self.balance += self.balance * self.int_rate
        return self

    @classmethod
    def display_all_accounts(cls):
        for acc in cls.bankAccounts:
            print(f'balance: {acc.balance} interest: {acc.int_rate}')


account1 = BankAccount(.05,1000)
account2 = BankAccount(balance=1000)

account1.deposit(200).deposit(10).deposit(2000).withdraw(200).yield_interest().display_account_info()
account2.deposit(200).deposit(200).withdraw(20).withdraw(20).withdraw(20).withdraw(20).yield_interest().display_account_info()

BankAccount.display_all_accounts()