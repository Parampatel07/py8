# Write a programe to findout wether the given number is pallindrome number or not using function 

def checkPallindrome(number):
     number = str(number)
     reversed_number = number[::-1]
     if number == reversed_number:
          print("It is pallindrome number ")
     else:
          print("It is not pallindrome number ")

checkPallindrome(151)
checkPallindrome(1510)