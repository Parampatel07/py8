from random import choice
import random
def generateNumbericOtp():
     # answer = random.randint(100000,999999)
     answer = str(random.randint(10,99)) + str(random.randint(10,99)) + str(random.randint(10,99))
     print(answer)

def generateAlphaOtp():
     alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','2','1','3','4','5','6','7','8','9','!','@','#','$','%']
     answer = choice(alphabet) + choice(alphabet) + choice(alphabet) + choice(alphabet) + choice(alphabet) + choice(alphabet) + choice(alphabet) + choice(alphabet)
     print(answer)

generateNumbericOtp()
generateAlphaOtp()