# Write a programe to findout greater number out of given 3 number 
number1 = int(input("Enter value of number 1 "))
number2 = int(input("Enter value of number 2 "))
number3 = int(input("Enter value of number 3 "))

if number1 == number2 :
     if number2 == number3:
          print("All are same ")
else:
     if number1 > number2:
          if number1 > number3:
               print("Number 1 is greater ")
          else :
               print("Number 3 is greater ")
     else:
          if number2 > number3:
               print("Number 2 is greater ")
          else:
               print("Number 3 is greater ")

