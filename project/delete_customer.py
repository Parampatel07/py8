from connection import myConnection
from view_customer import viewCustomer
def deleteCustomer():
     database = myConnection()
     viewCustomer()
     mycusor = database.cursor()
     id = int(input("Enter id to delete "))
     sql = "DELETE from customer where id = %s "
     value = [ id ]
     mycusor.execute(sql, value)
     database.commit()
     print("Customer Deleted Successfully....")
     viewCustomer()