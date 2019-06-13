class Order:

    def __init__(self, oid, price, restaurantName):
        self.oid = oid                          #Public
        self._price = price                     #Protected # may read but donot write
        self.__restaurantName = restaurantName  #Private   #

    def __show(self):
        print(self.oid, self._price,self.__restaurantName)

o1 = Order(101, 3000, "ABC Masala")
#print(o1.__dict__)
#print(o1.oid)
#print(o1._price)
#print(o1._Order__restaurantName)


# Sorting Algorithms : geeks4geeks
# Implement different Algorithms on List