import datetime
from datetime import date
from dateutil import parser

dict = {"startDateTimeLocal": "2021-12-28T11:57:00-06:00"}

time = parser.parse(dict["startDateTimeLocal"])

timeStr = time.strftime("%x")

today = date.today().strftime("%x")

if timeStr == today:
    print("Today")
else:
    print(timeStr)

print(time.ctime())
print(time.strftime("%x"))
print(today)
print(type(time))
