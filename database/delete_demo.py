import mysql.connector as con 

database = con.connect(host="localhost",port=3306,user="root",passwd="",database="django5")
print("Connection Established...")

mycursor = database.cursor()

id = int(input("Enter id to delete "))

sql = "DELETE from students where id = %s "

value = [ id ]

mycursor.execute(sql,value)

database.commit()
print(f"No of rows deleted is {mycursor.rowcount}")