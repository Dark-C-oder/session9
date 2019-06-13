"""
      Relationship Mapping
       HAS- A Mapping

            1 Engineer working on 1 project
            1 engineer working on many projects
            many engineers working on many projects

            1 customer has 1 address
            1 customer has many address
            Many customers have many Address

            customer
                name
                phone
                email
                address
            Driver
                name
                phone
                email

"""

class Customer:
    #constructor for standardisation
     def __init__(self, name, phone, email, address):
         self.name=name
         self.email=email
         self.phone=phone
         self.address = address

     def updateCustomerDetails(self, name, phone, email):
         self.name = name
         self.email = email
         self.phone = phone

     def showCustomersDetails(self):
         print("=====================")
         print("Name = \t", self.name)
         print("Phone = \t", self.phone)
         print("E-mail = \t", self.email)
         print("=====================")
         self.address.addressDetails()


class Address:
    # constructor for standardisation
    def __init__(self,adrsline, city, state):
        self.adrsline = adrsline
        self.city = city
        self.state = state

    def updateAddress(self,adrsline, city, state):
        self.adrsline = adrsline
        self.city = city
        self.state = state


    def addressDetails(self):
        print("=====================")
        print("adrsline = \t", self.adrsline)
        print("City = \t", self.city)
        print("State = \t", self.state)
        print("=====================")

a1 = Address("urban estate", "Ludhiana", "Punjab")
#a2 = Address("mall road", "manali", "himachal")
#
#adrslist [a1,a2]

c1 = Customer("John", "+91 99999 00000", "John@example.com",a1)
c2 = Customer("Rahul", "+91 99999 34440", "rahul@example.com",a1)

c1.showCustomersDetails()
c2.showCustomersDetails()
