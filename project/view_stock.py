from connection import myConnection
def viewStock():
     database = myConnection()
     mycursor = database.cursor(dictionary=True)
     sql = "SELECT * from stock "
     # sql = "SELECT * from stock where isdeleted = 0"
     mycursor.execute(sql)
     table = mycursor.fetchall()
     print("-"*91)
     print(f"| {"   id":5} | {'Product Name':15} | {'No of Item':15} | {'Price':15} | {'Isavaliable':15} |")
     for row in table:
          if row['isavaliable'] == 0:
               text_avaliable = "Yes"
          else:
               text_avaliable  = "No" 
          print(f"| {row['id']:5} | {row['name']:15} | {row['no_of_item']:15} | {row['price']:15} | {text_avaliable:15} |")
     print("-"*91)
