'''
Assignment: Store & Products
Objectives:
Practice creating classes
Practice associations between classes
Practice modularizing code
Start by creating a Store class that has 2 attributes: a name and a list of products. The name must be provided upon creation, but the products list should be empty.

Next, create a Product class that has 3 attributes: a name, a price, and a category. All of these should be provided upon creation.

Let's give some methods to our Product class:

update_price(self, percent_change, is_increased) - updates the product's price. If is_increased is True, the price should increase by the percent_change provided. If False, the price should decrease by the percent_change provided.
print_info(self) - print the name of the product, its category, and its price.
Let's also give some methods to our Store class:

add_product(self, new_product) - takes a product and adds it to the store
sell_product(self, id) - remove the product from the store's list of products given the id (assume id is the index of the product in the list) and print its info.
inflation(self, percent_increase) - increases the price of each product by the percent_increase given (use the method you wrote in the Product class!)
set_clearance(self, category, percent_discount) - updates all the products matching the given category by reducing the price by the percent_discount given (use the method you wrote in the Product class!)
'''


class Product:
    def __init__(self,name, price, category):
        self.name = name
        self.price = price
        self.category = category
        self.print_info()
    
    def update_price(self, percent_change, is_increased = True): 
        if (is_increased):
            self.price += self.price * percent_change
        else:
            self.price -= self.price * percent_change

        self.print_info()
        return self

    def print_info(self):
        print(f'{self.name}: {self.category} ${self.price} ')
    


class Store:
    def __init__(self, name):
        self.name = name
        self.products = []
    
    def add_product(self, new_product): 
        
        if (type(new_product) is Product ):
            self.products.append(new_product)
            print(f'{new_product.name} added')
        else:
            raise TypeError

        

    def sell_product(self, id):
        removed = self.products.pop(id)
        print(f'{removed.name} removed')
    
    def inflation(self, percent_increase):
        for product in self.products:
            product.update_price(percent_increase)


    def set_clearance(self, category, percent_discount):
        for product in self.products:
            if product.category == category:
                product.update_price(percent_discount,False)








iphone = Product('iPhone 12',500,'Smart Phone')
iphone.update_price(.1,False)

bestBuy = Store("Best Buy")
bestBuy.add_product(iphone)

bestBuy.inflation(0.1)
bestBuy.set_clearance("Smart Phone",0.1)
bestBuy.sell_product(0)