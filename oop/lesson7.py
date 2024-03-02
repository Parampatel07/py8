# Example of hierarchical Inheritance 
class Vehicle():
     def __init__(self,name):
          self.name = name
     def transport(self):
          print(f"{self.name} will transport ")
     
     def carry(self):
          print(f"{self.name} will carry goods ")

class Bike(Vehicle):
     def __init__(self,name):
          self.vehicle_name = name
          Vehicle.__init__(self,name)
     def door(self):
          print(f"{self.vehicle_name} have no doors")
     
     def wheels(self):
          print(f"{self.vehicle_name} have 2 wheels")

class Car(Vehicle):
     def __init__(self,name):
          self.name = name
          Vehicle.__init__(self,self.name)
     def door(self):
          print(f"{self.name} have 4 doors ")

     def wheels(self):
          print(f"{self.name} have 4 wheels ")

class Porcshe(Car):
     def __init__(self,name):
          self.name = name
          Car.__init__(self,self.name)
     def door(self):
          print(f"{self.name} have 2 doors ")
     def wheels(self):
          print(f"{self.name} has 4 wheels ")


print("======================Vehicle============================")
v1 = Vehicle('Road Vehicle')
v1.carry()
v1.transport()
print("======================Bike================================")
b1 = Bike('Shine')
b1.door()
b1.wheels()
b1.transport()
b1.carry()
print("======================Car================================")
c1 = Car('BMW')
c1.door()
c1.wheels()
c1.carry()
c1.transport()
print("======================Porsche=============================")
p1 = Porcshe('992 Gt3 rs')
p1.door()
p1.wheels()
p1.transport()
p1.carry()