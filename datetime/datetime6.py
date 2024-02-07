from datetime import datetime

date1 = datetime(2004,2,10)
date2 = datetime(2024,2,7)

print(date1)
print(date2)

difference = date2 - date1
print(difference)
total_month = int(difference.days / 30)
print(total_month)
total_year = int(difference.days / 365)
print(total_year)
total_hours = (difference.days * 24 )
print(total_hours)