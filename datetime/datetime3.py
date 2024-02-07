from datetime import datetime
from datetime import date

current_timestamp = datetime.now().timestamp()
print(current_timestamp)
current_timestamp = int(current_timestamp)
print(current_timestamp)


current_date = date.fromtimestamp(1207048652)
print(current_date)