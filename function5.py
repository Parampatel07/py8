# Example of keyword agrument 
# Write a programe to findout simple intrest using keyword argument function 

def simpleInterst(amount,rate_of_intrest,years):
     print("The value of amount is " ,amount)
     print("The value of rate_of_intrest is " ,rate_of_intrest)
     print("The value of years is " ,years)

     intrest = (amount * rate_of_intrest * years) / 100
     return intrest

amount = int(input('Enter value of amount '))
rate = int(input('Enter value of rate '))
years = int(input('Enter value of years '))

intrest = simpleInterst(years = years , amount = amount , rate_of_intrest = rate)
print("The value of simple intrest is " , intrest)