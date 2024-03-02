class bank:
     __balance = 500000000
     def __init__(self,name):
          self.name = name
     
     def getInfo(self):
          print(f"Name is {self.name} and balance is {self.__balance}")

     def addBalance(self,balance):
          self.__balance += balance
          print(f"New balance is " + str(self.__balance))

b1 = bank("hdfc")
b1.getInfo()
# print(b1.__balance)
b1.addBalance(5000)
print(b1._bank__balance)