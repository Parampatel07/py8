# Write a programe to findout smallest number out of given 3 numbers 
number1 = int(input("Enter value of number 1 "))
number2 = int(input("Enter value of number 2 "))
number3 = int(input("Enter value of number 3 "))

if number1 < number2 and number1 < number3:
     print("Number 1 is smallest ")
elif number2 < number1 and number2 < number3 :
     print("Number 2 is smallest ")
elif number3 < number1 and number3 < number2:
     print("Number 3 is smallest ")
else:
     print("All are same ")

print("Goodbyee...")