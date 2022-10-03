import datetime

now = datetime.datetime.now()
today = datetime.date.today()
month = datetime.datetime.now().month
year = datetime.datetime.now().year

print(now)  # is it now, now? I mean right now
print(f"Today is {today}.")
print(f"The month is {month}.")
print(f"The year is {year}.")
