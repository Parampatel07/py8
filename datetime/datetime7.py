from datetime import datetime

current = datetime.now()
print(current)

formate_date = current.strftime("%d - %m - %Y")
print(formate_date)

formate_time = current.strftime("%H : %M : %S")
print(formate_time)

formate = current.strftime("%d - %m - %Y  %H : %M : %S")
print(formate)