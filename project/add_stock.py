from connection import myConnection
def addStock():
     database = myConnection()
     mycursor = database.cursor()
     name =  input("Enter name of product ")
     no_of_item =  int(input("Enter no of item for product "))
     isavaliable =  int(input("Enter 0 if product is avaliable 1 if not avaliable  "))
     price =  int(input("Enter price of product "))
     sql = "INSERT into stock (name ,no_of_item , isavaliable , price ) VALUES ( %s , %s , %s , %s  )"
     data  = [ name , no_of_item , isavaliable , price ]
     mycursor.execute(sql,data)
     database.commit()
     print("Stock Added Successfully ")
