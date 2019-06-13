class Product:
    restaurantName = "ABC"

    #Constructor: When object will be created in memory
    #def __init__(self):
     #   self.name = "Dal Makhani"
      #  self.price = 200
        #FUNCTION

    def __init__(self,name,price):
        self.name=name
        self.price = price

    def showPrint(self):
        print(self.name, self.price, Product.restaurantName)

    # Destructor : when object will be deleted in memory
    def __del__(self):
        print("Product Deleted", self)


p1 = Product("dal makhani", 200)
p2 = Product("paneer", 500)

print(hex(id(p1)))
print(hex(id(p2)))

print(p1.__dict__)
print(p2.__dict__)

p1.showPrint()
p2.showPrint()

print("ThankYou")