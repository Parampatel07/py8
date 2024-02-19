# Example of Multilevel inheritance 
class Person:
     def __init__(self,name):
          self.name = name
     def talk(self):
          print(f"{self.name} can talk ")
     def walk(self):
          print(f"{self.name} can walk ")

class Student(Person):
     def __init__(self,name):
          self.name = name
          Person.__init__(self,self.name)
     def read(self):
          print(f"{self.name} can read")
     def write(self):
          print(f"{self.name} can write ")

class Teacher(Student):
     def __init__(self,name):
          self.name = name
          Student.__init__(self,self.name)
     def teach(self):
          print(f"{self.name} can teach ")
     
     def test(self):
          print(f"{self.name} will take test ")

print("=======================Person====================")
p1 = Person('Param Patel')
p1.talk()
p1.walk()
print("========================Student===================")
s1 = Student('Param Patel')
s1.read()
s1.write()
s1.walk()
s1.talk()
print("========================Teacher=====================")
t1 = Teacher('Param Patel')
t1.read()
t1.write()
t1.teach()
t1.test()
t1.walk()
t1.talk()