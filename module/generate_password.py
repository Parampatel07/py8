import string
from random import randint 

def generatePassword(lenght=10):
     alphabets = string.ascii_lowercase + string.ascii_uppercase + string.digits
     # print(alphabets)
     password = []
     size = len(alphabets) - 1 
     for i in range(0,lenght):
          password.append(alphabets[randint(0,size)])
     print(password)
     answer = "".join(password)
     print(answer)

generatePassword()
