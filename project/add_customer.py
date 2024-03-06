from connection import myConnection

def addCustomer():
     name = input("Enter name of customer ")
     phone = int(input("Enter phone number of customer "))
     email = input("Enter email address of customer ")
     gender = int(input("Enter gender of customer enter 1 for male and 0 for female "))
     database = myConnection()
     sql = "INSERT INTO customer ( name , phone , email , gender ) VALUES ( %s , %s ,%s , %s )"
     value =  [ name , phone , email , gender  ]
     mycursor = database.cursor()
     mycursor.execute(sql,value)
     database.commit()
     print("===================================================")
     print("Customer Added Sucessfully ")
     print("===================================================")


# addCustomer()