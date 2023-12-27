# Write a programe to print following pattern 
# 1 8 27 64 .... 10000

number = 1 
answer = 0 

print(number,end=' ')
while answer < 9261:
     number = number+ 1 # 2
     answer  = number * number * number
     print(answer,end=' ')
# number = number + 1 
# answer = number * number * number
# print(answer)
# number = number + 1 
# answer = number * number * number
# print(answer)