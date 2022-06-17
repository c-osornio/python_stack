# Create a Product class with 3 attributes
#SENSEI BONUS: Update the product class to give each product a unique id. Update the sell_product method to accept the unique id.
class Product:
    def __init__(self, name, price, category, id):
        self.name = name
        self.price = price
        self.category = category
        self.id = id
# Add the update_price method to the Product class
    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            x = self.price + (self.price * percent_change)
            self.price = round(x, 2)
            self.print_info()
            return self
        else: 
            x = self.price - (self.price * percent_change)
            self.price = round(x, 2)
            self.print_info()
            return self
# Add the print_info method to the Product class
    def print_info(self):
        print(f'Current price for {self.name} {self.category} are ${self.price}!')
        return self