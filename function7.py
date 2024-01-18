# Example of function expotiental calc using recursion 

def calc_factorial(number):
     if number == 1 :
          return 1 
     else:
          return (number * calc_factorial(number - 1))

number = int(input("Enter value of number "))
answer = calc_factorial(number)
print(answer)