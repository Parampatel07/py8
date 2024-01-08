# Write a programe to findout how many vowels does the string have take string from user 
string = input("Enter any string ")
print(string)
vowels = ['a','e','i','o','u']
count = 0
for value in string:
     print(value)
     if value in vowels:
          count+=1

print("Total number of vowels are : " , count)