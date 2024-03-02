import mysql.connector as con 

database = con.connect(host="localhost",port=3306,user="root",passwd="",database="django5")
print("Connection established...")

name = input("Enter your name ")
email = input("Enter your email")
password = input("Enter your password")
phone = input("Enter your phone")
address = input("Enter your address")
dob = input("Enter your dob")
gender = int(input("Enter your gender Enter 1 for Male and 0 for female"))

mycursor = database.cursor()

sql = "INSERT into students ( name , email , password, phone , dob, address, gender ) VALUES (%s,%s,%s,%s,%s,%s,%s)"

data = [ name ,email , password , phone , dob , address , gender ]

mycursor.execute(sql,data)

database.commit()
print("Student Insert Successfully ")