# Write a programe to findout factorial of given number 
number = int(input("Enter value of number "))


count = 2
answer = number * (number - 1)
while count < number :
     answer = answer * (number - count)
     count+=1
# answer = answer * (number - 3)
# answer = answer * (number - 4)
print(answer)