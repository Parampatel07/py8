class Person:
     def walk(self):
          print("i can walk ")
     def talk(self):
          print("i can talk ")

class Student():
     def read(self):
          print("i can read ")

     def write(self):
          print("i can write")

class Teacher(Person,Student):
     def teach(self):
          print("I can teach ")

t1 = Teacher()
t1.teach()
t1.read()
t1.write()
t1.walk()
t1.talk()