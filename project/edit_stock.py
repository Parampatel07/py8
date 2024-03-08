from connection import myConnection
from view_stock import viewStock
def editStock():
     database = myConnection()
     mycursor = database.cursor(dictionary=True)
     viewStock()
     stockid = int(input("Enter stockid to edit "))
     sql = "SELECT * from stock where id = %s "
     value = [ stockid ]
     mycursor.execute(sql,value)
     row = mycursor.fetchall()
     name = input("Enter name ")
     no_of_item = input("Enter no of item ")
     isavaliable = input("Enter 0 if avaliable and 1 if not avaliable ")
     price = input("Enter price ")
     if name == '' or name == " ":
          name = row[0]['name']
     if no_of_item == '' or no_of_item == " ":
          no_of_item = row[0]['no_of_item']
     if isavaliable == '' or isavaliable == " ":
          isavaliable = row[0]['isavaliable']
     if price == '' or price == " ":
          price = row[0]['price']
     sql = " UPDATE stock set name = %s , price = %s , isavaliable = %s ,no_of_item = %s where id = %s"
     value= [ name , price , isavaliable ,no_of_item ,stockid  ]
     mycursor.execute(sql,value)
     database.commit()
     viewStock()
     print("Stock Updated Sucessfully ")


