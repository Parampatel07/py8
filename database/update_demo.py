import mysql.connector as con 

database = con.connect(host="localhost",port=3306,user="root",passwd="",database="django5")
print("Connection established...")

id = int(input("Enter your id to update "))
name = input("Enter your name ")
email = input("Enter your email")
password = input("Enter your password")
phone = input("Enter your phone")
address = input("Enter your address")
dob = input("Enter your dob")
gender = int(input("Enter your gender Enter 1 for Male and 0 for female"))

mycursor = database.cursor()

sql = "Update students set name = %s , email = %s , password = %s , phone = %s , address = %s , dob = %s , gender = %s where id = %s "

data = [ name ,email , password , phone , address , dob , gender , id ]

mycursor.execute(sql,data)

database.commit()
print("Student Updated Successfully ")