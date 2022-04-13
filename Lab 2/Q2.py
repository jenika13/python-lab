#to count the number of characters (character frequency) 

str = input("Enter a string : ")

frequency_table = {}

for a in str:
    frequency_table[a]=frequency_table.get(a,0)+1
print("Character frequency table for {} is {}".format(str, frequency_table))