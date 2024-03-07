from connection import myConnection
from view_customer import viewCustomer
def editCustomer():
     database = myConnection()
     viewCustomer()
     mycursor = database.cursor(dictionary=True)
     customerid = int(input("Enter id to edit customer \n"))
     sql = "SELECT * from customer where id = %s "
     value = [ customerid ]
     mycursor.execute(sql,value)
     row = mycursor.fetchall()
     print(row)
     prev_name = row[0]['name']
     prev_phone = row[0]['phone']
     prev_email = row[0]['email']
     prev_gender = row[0]['gender']
     name = input("Enter name of customer ")
     phone = int(input("Enter phone number of customer "))
     email = input("Enter email address of customer ")
     gender = int(input("Enter gender of customer enter 1 for male and 0 for female "))
     if name == '' or name == ' ':
          name = prev_name
     # if phone == ' ' or phone== '':
     #      phone = prev_phone
     if email == ' ' or email == '':
          email = prev_email 
     # if gender == ' ' or gender == '':
     #      gender = prev_gender 
     sql = "UPDATE customer set name = %s , phone  = %s , email = %s , gender = %s where id = %s "
     value = [ name , phone , email , gender , customerid ]
     mycursor.execute(sql,value)
     database.commit()
     print("Customer Updated Successfully ")
     viewCustomer()