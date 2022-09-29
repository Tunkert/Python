from datetime import datetime

the_date = datetime.now()
the_day = the_date.day
the_month = the_date.month
the_year = the_date.year
the_weekday = the_date.isoweekday()

print(f"Today's date is {the_date}")
print(f"More specifically, today's date is {the_month}/{the_day}/{the_year}!")
print(f"The day of the week is {the_weekday}.")  # gives a number (maybe use a conditional)
