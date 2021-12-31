class User:
    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance
    
    def make_deposit(self, amount):
        self.balance += amount
    
    def make_withdrawal(self, amount):
        self.balance -= amount

    def display_user_balance(self):
        print(f'{self.name} has ${self.balance}')

    def transfer_money(self,other_user,amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)



reuben = User("Reuben",1000)

reuben.make_deposit(1000)
reuben.display_user_balance()

reuben.make_withdrawal(500)
reuben.display_user_balance()

judah = User("Judah")

judah.display_user_balance()

reuben.transfer_money(judah,1000)

reuben.display_user_balance()
judah.display_user_balance()

