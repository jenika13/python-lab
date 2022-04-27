#to read a file line by line store it into a variable.

f = open("C:/Users/acer/Desktop/Lab/Python/Lab 3/test.txt", "r")
lines=f.readlines()
string=""
s=string.join(lines)
print(s)
f.close()