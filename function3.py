# Write a programe to findout product execpt self from list 
# number = [1,2,4,5,10]
# answer = [400,200,100]

number = [1,2,4,5,10]
answer = []
flash = 0
while flash < len(number):
     temp = 1 
     count = 0
     while count < len(number):
          temp = temp * number[count] 
          count+=1
     answer.append(int(temp / number[flash]))
     flash+=1
print(answer)
# temp = 1
# count = 0
# while count < 5 : 
#      temp = temp * number[count]
#      count+=1
# answer.append(int(temp / number[1]))
# print(answer)
# temp = 1
# count = 0
# while count < 5 :
#      temp = temp * number[count]
#      count+=1
# answer.append(int(temp / number[2]))
# print(answer)