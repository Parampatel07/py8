import mysql.connector as con

def myConnection():
     database = con.connect(host="localhost",user="root",passwd="",database="python8",port=3306)
     print("connection established... ")
     return database 
