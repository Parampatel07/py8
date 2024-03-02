import mysql.connector as con 

database = con.connect(host="localhost",user="root",passwd="",port=3306,database="django5")
print("Connection established... ")