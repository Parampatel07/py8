# write a program to findout all the perfect numbers between given range

for count in range(1,999999999999):
     number = count
     divisor = []
     answer = 0
     square = number * 2 
     for i in range(1,number+1):
          if number % i == 0:
               divisor.append(i)
     for value in divisor:
          answer += value 
     if square == answer:
          print("It is perfect number : " , number)
# if number % 2 == 0:
#      divisor.append(2)
# if number % 3 == 0:
#      divisor.append(3)
# if number % 4 == 0:
#      divisor.append(4)