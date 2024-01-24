name = "The EasyLearn Academy "

upper_string = str.upper(name)
print(upper_string)
print(name)

lower_string = str.lower(name)
print(lower_string)

data = "alpha12313"
print(str.isalnum(data))
data = "alpha"
print(str.isalpha(data))
data = "AlpHabet"
print(str.islower(data))
data = "12313ABC"
print(str.isnumeric(data))
data = " "
print(str.isspace(data))
data = "Alphabet are 26"
print(str.istitle(data))
data = "THE EASYLEARN"
print(str.isupper(data))
data = "Param patel"
print(len(data))

data = ["red","blue","green","orange","yellow","black"]
seperator = ' + '
result = seperator.join(data)
print(result)

result = result.replace("+","--")
print(result)

print(result.split(' '))
print(result.split("--"))
print(result.split("--",3))
print(result.split("+"))