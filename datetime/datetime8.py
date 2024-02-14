from datetime import datetime
from datetime import date
# formate_date = datetime.strptime("2-12-2024 10:15:20","%d-%m-%Y %H:%M:%S")
# print(formate_date)
print("Enter your birth date ")
day = int(input("Enter your Birth day "))
month = int(input("Enter your Birth month "))
year = int(input("Enter your birth year "))

string_date = f'{day}-{month}-{year}'
# print(string_date)

object_date = date(year,month,day)
# print(object_date)

object_current = date.today()
# print(object_current)

difference = object_current - object_date
print(difference)

difference_hours = difference.days * 24 
print("Total number of hours " + str(difference_hours))