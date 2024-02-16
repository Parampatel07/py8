class Person:
     def __init__(self,name):
          self.my_name = name
          print("Constructor called... ")
      
     def walk(self):
          print("I can walk " + self.my_name )
          
     def talk(self):
          print("I can talk")

p1 = Person(name="Param Patel")
p2 = Person(name="Jhon doe")
p1.walk()
p1.talk()
p2.walk()
p2.talk()