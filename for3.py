# Write a programe to findout how many vowels does the string have take string from user and also count each number of vowels also count space 
string = input("Enter any string ")
print(string)
string = string.lower()
count_vowel = {'a' : 0 , 'e' : 0 , 'i':0,'o':0,'u':0,' ':0}
vowels = ['a','e','i','o','u',' ']
count = 0
for value in string:
     print(value)
     if value in vowels:
          count_vowel[value]+=1

print("Total number of vowels are : " , count_vowel)