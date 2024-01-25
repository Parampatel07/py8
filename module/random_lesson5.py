# Write a programe to create a quiz game 
# [{ 'what is your name' : 'param' }]

import random

question = [ { 'How many time zones are there in Russia?' : '11' } , 
     { 'What’s the national flower of Japan? ' :  'cherry blossom' , }, 
     {'How many stripes are there on the US flag? ' : '13'}, 
     { 'What’s the national animal of Australia? ' : 'kangaroo' } ,
     { 'How many days does it take for the Earth to orbit the Sun ?' : '365'},
]
score = 0
asked_question = []
number_of_question = 0
# choice = random.choice(question)
# asked_question.append(choice)
# # print(choice)
# user_question = list(choice.keys())
# answer = list(choice.values())
# number_of_question +=1
# print(user_question[0])
# user_answer = input("Enter your answer ")
# if user_answer == answer[0]:
#      score+=1
# print(score)

while number_of_question < 5 :
     choice = random.choice(question)
     if choice not in asked_question:
          # print(choice)
          asked_question.append(choice)
          user_question = list(choice.keys())
          answer = list(choice.values())
          number_of_question +=1
          print(user_question[0])
          user_answer = input("Enter your answer ")
          if user_answer == answer[0]:
               score+=1
          # print(score)

if score < 3:
     print("Better luck next time ")
else:
     print('Congratulation !!')