class Product: 
    def __init__(self, price, stock, product_name):
        self.__price = price
        self.__stock = stock
        self.product_name = product_name
        
    def get_price(self):
        return self.__price
    
    def get_stock(self): 
        return self.__stock
    
    def reduce_stock(self, quantity): 
        self.__stock = self.__stock - quantity
        
    def get_discounted_price(self): 
        return self.__price

class Electronics(Product): 
    def __init__(self, price, stock, product_name):
        super().__init__(price, stock, product_name)
        # self.discount = discount
        
    def get_discounted_price(self):
        return super().get_price() * 0.90

class Clothing(Product): 
    def __init__(self, price, stock, product_name):
        super().__init__(price, stock, product_name)
        
    def get_discounted_price(self):
        return super().get_price() * 0.80
    
class Grocery(Product): 
    def __init__(self, price, stock, product_name):
        super().__init__(price, stock, product_name)
        # self.discount = discount
        
    def get_discounted_price(self):
        return super().get_price() * 0.95


class Cart: 
    def __init__(self):
        self.products = {}
    
    def add_item(self, product, quantity):
        if quantity > product.get_stock():
            print("Not enough stock")
            return
        if product in self.products:
            self.products[product] += quantity
            
        else: 
            self.products[product] = quantity
        print(f'You have added successfully {quantity} {product.product_name} in your cart')

    
    def remove_item(self, product, quantity):
        if product not in self.products:
            print(f'{product.product_name} is not on your cart!')
            return
        
        if quantity > self.products[product]:
            print(f"You only have {self.products[product]} {product.product_name} in cart!")
            return
        
        if quantity == self.products[product]:
            del self.products[product]
            print(f"Removed all {product.product_name} from cart")
        else:
            self.products[product] -= quantity
            print(f"Removed {quantity} {product.product_name} from cart")

    
    
    def checkout(self):
        if not  self.products:
            print("Your Cart is empty")
            return
        
        print("===== RECEIPT =====")
        total = 0
        
        for product, quantity in self.products.items():
            item_price = product.get_discounted_price()
            item_total = item_price  * quantity
            print(f"{product.product_name} x {quantity} = Rs.{item_total}")
            total += item_total
        
        
        print(f"\nTotal: Rs.{total}")
        print("===================")
        for product, quantity in self.products.items():
            #call reduce_stock on the product
            product.reduce_stock(quantity)

        self.products = {}
        print("Thank you for shopping!")


iphone = Electronics(price=50000, stock=10, product_name="iPhone 15")
tshirt = Clothing(price=1000, stock=20, product_name="Cotton T-Shirt")
milk = Grocery(price=60, stock=30, product_name="Milk 1L")


cart = Cart()


print("\n--- Adding items to cart ---")
cart.add_item(iphone, 2)      
cart.add_item(tshirt, 3)       
cart.add_item(milk, 5)      


print("\n--- Removing items ---")
cart.remove_item(iphone, 1)   
cart.remove_item(milk, 2)    

print("\n--- Checkout ---")
cart.checkout()

print("\n--- Stock after checkout ---")
print(f"iPhone stock: {iphone.get_stock()}")
print(f"T-Shirt stock: {tshirt.get_stock()}")
print(f"Milk stock: {milk.get_stock()}")