#Python program to convert unix timestamp string to readable date

from datetime import date

timestamp = date.fromtimestamp(1650910000)
print("Date =", timestamp)