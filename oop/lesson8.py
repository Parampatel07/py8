class account:
     def __init__(self,name,amount):
          self.name = name
          self.__amount = amount 
     def getInfo(self):
          print(f"Name is {self.name} amount is {self.__amount}")

     def updateAmount(self,new_amount):
          self.__amount = new_amount

a1 = account("Param Patel",10000)
a1.getInfo()
a1.name = 'Param'
a1.__amount = 20000
a1.getInfo()
a1.updateAmount(20000)
a1.getInfo()