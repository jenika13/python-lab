#to read last n lines of a text file

f = open("C:/Users/acer/Desktop/Lab/Python/Lab 3/test.txt", "r")
n = int(input("Enter the number of lines to read : "))
lines=f.readlines()
last_line=lines[-n:]
string=""
s=string.join(last_line)
print(s)
f.close()