from connection import myConnection
def dailyBill():
     database = myConnection()
     mycursor = database.cursor(dictionary=True)
     sql = "SELECT sum(amount) as total from bill where DATE(CURRENT_DATE) = DATE(bill_date)"
     mycursor.execute(sql)
     table = mycursor.fetchall()
     # print(table)
     if table[0]['total'] == None :
          print("No entry found ")
     else:
          print("-"*24)
          print(f"| {"Total daily Income":20} |")
          for row in table:
               print(f"| {row['total']:20} |")
          print("-"*24)

