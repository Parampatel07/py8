# Example of function 

def getAdd(number1 , number2):
     answer = number1 + number2 
     return answer

a = int(input("Enter value of number 1 "))
b = int(input("Enter value of number 2 "))
result = getAdd(a,b)
print("The value of answer is " , result)