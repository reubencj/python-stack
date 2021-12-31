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





class User:
    def __init__(self, name):
        self.name = name
        self.account = BankAccount()
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        print(f'{self.name} has ${self.account.balance}')

    def transfer_money(self,other_user,amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        return self




reuben = User("Reuben")

reuben.make_deposit(1000)
reuben.display_user_balance()

reuben.make_withdrawal(500).make_deposit(90000)
reuben.display_user_balance()

judah = User("Judah")

judah.display_user_balance()

reuben.transfer_money(judah,1000)

reuben.display_user_balance()
judah.display_user_balance