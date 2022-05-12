#Python program to get week number from 16/06/2015

import datetime

dt = datetime.date(2015,6,16)
weekno = dt.strftime("%U")
print("Week number of the year: ",weekno)