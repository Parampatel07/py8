# Write a programe to print first 20 the prime number
count = 0
prime_number = []
flash = 2
while count < 20:
     number = flash
     answer = False 
     for i in range(2,number):
          if number % i == 0:
               answer = True
               break
     if answer == False:
          count+=1
          prime_number.append(number)
     flash+=1

print(prime_number)