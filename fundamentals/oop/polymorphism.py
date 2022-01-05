class Person:
    def __init__(self, name):
        self.name = name
        
    def pay_bill(self):
        raise NotImplementedError

class Millionaire(Person):
    def __init__(self, name, millions):
        super().__init__(name)
        self.millions = millions

    def sayHello(self):
        print(f'hi my name is {self.name} and I am worth ${self.millions} Million')
    
    def pay_bill(self, amount):
        total = self.millions * 1000000
        total -= amount
        self.millions = total - 1000000
        print(f'{self.name} paid ${amount}, total wealth is ${self.millions} Million')




reuben = Millionaire("Reuben John",2)
reuben.sayHello();
reuben.pay_bill(1000000);