import random

number_list = []
for i in range(0,50):
     number = random.random() 
     number = round(number,2)
     number_list.append(number)
# print(number_list)

print(round(random.uniform(10,13),2))
