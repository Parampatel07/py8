from connection import myConnection
def monthlyBill():
     database = myConnection()
     mycursor = database.cursor(dictionary=True)
     sql = "SELECT sum(amount) as total from bill where MONTH(CURRENT_DATE) = MONTH(bill_date) and YEAR(CURRENT_DATE) = YEAR(bill_date)"
     mycursor.execute(sql)
     table = mycursor.fetchall()
     if table[0]['total'] == None :
          print("No entry found ")
     else:
          print("-"*24)
          print(f"| {"Total monthly Income":20} |")
          for row in table:
               print(f"| {row['total']:20} |")
          print("-"*24)
