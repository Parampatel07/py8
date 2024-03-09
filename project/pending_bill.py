from connection import myConnection
def pendingBill():
     database = myConnection()
     mycursor = database.cursor(dictionary=True)
     sql = "SELECT b.* , c.name as customer_name from bill b , customer c where b.status = 2 and b.customerid = c.id"
     mycursor.execute(sql)
     table = mycursor.fetchall()
     # print(table)
     print("-"*129)
     print(f"| {"   id":5} | {'Customer Name':15} | {'Amount':25} | {'Discount':15} | {'Bill Date':20} | {'Mode Of Payment':20} | {'Status':7} |")
     for row in table:
          if row['mode_of_payment'] == 0:
               text_mode = "Cash"
          else:
               text_mode  = "Online Transfer " 
          if row['status'] == 1 :
               text_status = "Paid"
          else:
               text_status = "Pending"
          # print(row)
          print(f"| {row['id']:5} | {row['customer_name']:15} | {row['amount']:25} | {row['discount']:15} | {row['bill_date'].strftime("%m/%d/%Y, %H:%M:%S"):20} | {text_mode:20} | {text_status:7} |" )
     print("-"*129)

