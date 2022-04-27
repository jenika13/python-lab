#to read a file line by line and store it in list

f = open("C:/Users/acer/Desktop/Lab/Python/Lab 3/test.txt", "r")
lines=f.readlines()
line=[lines]
print(line)
f.close()