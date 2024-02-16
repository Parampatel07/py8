class Person:
     def __init__(self,name):
          self.name = name 
     def displayNamePerson(self):
          print(f"My name as person " + self.name)

class Student(Person):
     def __init__(self,name,marks):
          Person.__init__(self,name)     
          self.marks = marks

     def displayName(self):
          print(f"My name is " + self.name)

     def displayMarks(self):
          print(f"My marks are " + str(self.marks)) 


s1 = Student("Param Patel",99)
s1.displayName()
s1.displayMarks()
s1.displayNamePerson()

print("==========================================")
p1 = Person("Param ")
p1.displayNamePerson()