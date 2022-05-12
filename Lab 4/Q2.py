#Python program to subtract five days from current date

from datetime import date,timedelta

current_date = date.today()
dt = current_date - timedelta(5)
print("Current date : ",current_date)
print("After subtracting 5 days : ",dt)   