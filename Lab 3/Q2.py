#to read first n lines of a file

f = open("C:/Users/acer/Desktop/Lab/Python/Lab 3/test.txt", "r")
n = int(input("Enter the number of lines to read : "))
for i in range(n):
    lines=f.readline()
    print(lines)
f.close()