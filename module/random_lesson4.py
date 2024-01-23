from random import shuffle
from random import sample
colors  = ['red','green','blue' ,'yellow','black','orange','white']
colors_length = len(colors)

duplicate = sample(colors,colors_length)
print(colors)
print(duplicate)
# shuffle(colors)
# print(colors)

