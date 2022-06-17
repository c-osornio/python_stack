import store
import products
# # NINJA BONUS: Modularize your code into 3 separate files
# Test out your classes by creating an instance of the Store and a few instances of the Product class, add those instances to the store instance, and then test out the methods.
nikes = products.Product("Nike", 59.99, "shoes", 12345)
nikes.print_info()
nikes.update_price(.20, False)


FootLocker = store.Store("Foot Locker")
FootLocker.add_product("Adidas", "Ultra-Boost", 89.99, "shoes", 12346)
FootLocker.sell_product(12346)
print(FootLocker.products)
FootLocker.add_product("NewBalance", "Fresh Foam X", 159.99, "shoes", 12347)
FootLocker.add_product("Puma", "Suede Classic XXI", 70, "shoes", 12348)
FootLocker.inflation(.25)
FootLocker.set_clearance("shoes", .75)
