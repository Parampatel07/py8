from connection import myConnection
def yearlyBill():
     database = myConnection()
     mycursor = database.cursor(dictionary=True)
     sql = "SELECT sum(amount) as total from bill where YEAR(CURRENT_DATE) = YEAR(bill_date)"
     mycursor.execute(sql)
     table = mycursor.fetchall()
      if table[0]['total'] == None :
          print("No entry found ")
     else:
          print("-"*24)
          print(f"| {"Total yearly Income":20} |")
          for row in table:
               print(f"| {row['total']:20} |")
          print("-"*24)

