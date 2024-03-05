import mysql.connector as con 

database = con.connect(host="localhost",port=3306,user="root",passwd="",database="django5")
print("connection established ")

id = int(input("Enter value of id "))
mycursor = database.cursor(dictionary=True)

sql = "Select * from students where id = %s"

value = [ id ]

mycursor.execute(sql,value)

table = mycursor.fetchall()

print(table)
for row in table:
     print(f"{row['id']}  {row['name']:10} {row['email']:15} {row['password']:8} {row['phone']:12} {row['dob']:10} {row['address']:25} {row['gender']:5}")