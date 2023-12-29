# write a programe to findout how many odd and even number does the list have 
numbers = [1,69,6,4563,2,4,862,36,4,9,51,35,69,8,456]

odd_count = 0
count = 0 
flash = 0
print(len(numbers))

while flash < len(numbers):
     if numbers[flash] %2 == 0:
          count += 1  
     else:
          odd_count +=1
     flash+=1

print("total even number " , count)
print("total odd number " , odd_count)