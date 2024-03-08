from connection import myConnection
from view_stock import viewStock
def deleteStock():
     database = myConnection()
     mycursor = database.cursor()
     viewStock()
     stockid  = int(input("Enter id to delete "))
     sql = "DELETE from stock where id = %s "
     # sql = "Update stock set isdeleted= 0 where id  = %s "
     value = [ stockid ]
     mycursor.execute(sql,value)
     database.commit()
     viewStock()
     print("Stock deleted Sucessfully ")
