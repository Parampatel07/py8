# Write a programe to findout power and exponent of given number 
# base = 5 
# power = 3 
# 5 * 5 * 5 = 125 
base = int(input("Enter value of base "))
power = int(input("Enter value of power "))


count = 2

answer = base * base 
while count < power:
     answer = answer * base 
     count+=1
# answer = answer * base 
# answer = answer * base 
print("answer : ",answer)