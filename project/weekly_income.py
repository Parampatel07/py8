from connection import myConnection
def weeklyBill():
     database = myConnection()
     mycursor = database.cursor(dictionary=True)
     sql = "SELECT sum(amount) as total from bill where WEEK(CURRENT_DATE) = WEEK(bill_date) and YEAR(CURRENT_DATE) = YEAR(bill_date) and MONTH(CURRENT_DATE) = MONTH(bill_date)"
     mycursor.execute(sql)
     table = mycursor.fetchall()
     if table[0]['total'] == None :
          print("No entry found ")
     else:
          print("-"*24)
          print(f"| {"Total Weekly Income":20} |")
          for row in table:
               print(f"| {row['total']:20} |")
          print("-"*24)

