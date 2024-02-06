import datetime
         # module.class.method 
current = datetime.datetime.now()
print(current)
current_date = datetime.date.today()
print(current_date)
current_hour = current.hour
current_minute = current.minute
current_second = current.second
# print(current_hour)
# print(current_minute)
# print(current_second)
print(f"{current_hour} : {current_minute} : {current_second}")