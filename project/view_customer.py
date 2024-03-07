from connection import myConnection

def viewCustomer():
     database = myConnection()
     mycursor = database.cursor(dictionary=True)
     sql = "SELECT * from customer"
     mycursor.execute(sql)
     table = mycursor.fetchall()
     # print(table)
     print("-----------------------------------------------------------------------------------")
     print(f"| {"   id":5} | {'name':15} | {'email':25} | {'phone':15} | {'gender':7} |")
     for row in table:
          if row['gender'] == 0:
               text_gender = "Female"
          else:
               text_gender  = "Male" 
          print(f"| {row['id']:5} | {row['name']:15} | {row['email']:25} | {row['phone']:15} | {text_gender:7} |")
     print("-----------------------------------------------------------------------------------")
