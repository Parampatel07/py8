# Write a programe to create a conversion calc for gb 

def conversion(gb):
     # gb to mb 
     mb = gb * 1000
     # gb to kb 
     kb = gb * 1000000
     # gb to bytes 
     bytes = gb * 1000000000
     return mb,kb,bytes

def arbitary(*names):
     print(names)
     for i in names:
          print("Hello i am " , i)


gb = int(input("Enter value of gb "))
converted_list = conversion(gb)
print(converted_list)

arbitary("param","dhruv","rakesh","ankit")