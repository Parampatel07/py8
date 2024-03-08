from connection import myConnection
from view_customer import viewCustomer
import qrcode
def addBill():
     database = myConnection()
     mycursor = database.cursor(dictionary=True)
     viewCustomer()
     customerid = int(input("Enter customer id "))
     amount = int(input("Enter amount "))
     discount = int(input("Enter discount in rupees "))
     mode_of_payment = int(input("Enter 0 for cash and 1 for online transfer "))
     status = int(input("Enter 1 for paid bill 2 for pending payment "))
     sql = "INSERT into bill (customerid , amount ,discount ,mode_of_payment,status) VALUES (%s , %s ,%s ,%s ,%s) "
     data = [ customerid , amount , discount , mode_of_payment , status ]
     mycursor.execute(sql,data)
     lastid = mycursor._last_insert_id
     print(lastid)
     database.commit()
     sql = "SELECT name from customer where id = %s "
     value = [ customerid  ]
     mycursor.execute(sql,value)
     row = mycursor.fetchall()
     if mode_of_payment == 0 :
          mode_of_payment = "cash"
     elif mode_of_payment == 1 :
          mode_of_payment = "Online Transfer"
     if status == 1 :
          status = "Paid"
     elif status ==2 :
          status = "Pending "
     img = qrcode.make(f' customerid = {customerid} \n customername = {row[0]['name']}  \n amount = {amount} \n discount = {discount} \n mode_of_payment = {mode_of_payment} \n status = {status} ')
     img.save(f"qr_code/{lastid}.png")
     print("Bill added Successfully ")
