import products
# Create a Store class with 2 attributes
class Store:
    def __init__(self, name):
        self.name = name
        self.products = []
# Add the add_product method to the Store class
    def add_product(self, new_product, name, price, category, id):
        new_product = products.Product(name, price, category, id)
        self.products.append(new_product)
        return self
# Add the sell_product method to the Store class
    def sell_product(self, id):
        for product in self.products:
            if product.id == id:
                product.print_info()
                self.products.remove(product)
        return self
# NINJA BONUS: Add the inflation method to the Store class
    def inflation(self, percent_increase):
        for product in self.products:
            product.price += (product.price * percent_increase)
            print(f"Due to inflation, new price for {product.name} {product.category} are ${product.price}!")
# NINJA BONUS: Add the set_clearance method to the Store class
    def set_clearance(self, category, percent_discount):
        for product in self.products:
            if product.category == category:
                product.price = product.update_price(percent_discount, False)