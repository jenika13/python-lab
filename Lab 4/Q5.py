#Python program to get days between two dates.

from datetime import date

t1 = date(year = 2001, month = 2, day = 28)
t2 = date(year = 2000, month = 2, day = 28)
t3 = t1 - t2
print("The difference between given dates : ",t3)