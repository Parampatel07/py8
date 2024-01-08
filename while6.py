# write a programe to findout how many odd and even number does the list have 
numbers = [1,69,6,4563,2,4,862,36,4,9,51,35,69,8,456]
even_list = []
odd_list = []
odd_count = 0
count = 0 
flash = 0
print(len(numbers))
while flash < len(numbers):
     if numbers[flash] %2 == 0:
          count += 1  
          even_list.append(numbers[flash])
     else:
          odd_count +=1
          odd_list.append(numbers[flash])
     flash+=1
print("even list is " , even_list)
print("odd list is " , odd_list)
print("total even number " , count)
print("total odd number " , odd_count)