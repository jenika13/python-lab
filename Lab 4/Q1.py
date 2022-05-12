#Write a Python script to display the

from datetime import datetime
current=datetime.now()

#Current date and time
date_time=current.strftime("%m/%d/%Y, %H:%M:%S")
print("Date and time: ",date_time)

#Current year
year=current.strftime("%Y") 
print("Year: ",year)

#Month of year
month=current.strftime("%B")
print("Month: ",month)

#Week number of the year
weekno=current.strftime("%U")
print("Week number of the year: ",weekno)

#Weekday of the week
weekday=current.strftime("%A")
print("Weekday of the week:",weekday)

#Day of year
dayyear=current.strftime("%j")
print("Day of year: ",dayyear)

#Day of the month
daymnth=current.strftime("%d")
print("Day of the month: ",daymnth)

#Day of the week
dayweek=current.strftime("%w")
print("Day of the week:",dayweek)