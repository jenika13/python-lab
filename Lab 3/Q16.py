#Python program to remove newline characters from a file.

f = open("C:/Users/acer/Desktop/Lab/Python/Lab 3/test.txt", "r")
lines = f.readlines()
for i in lines:
    rline = ([i.rstrip('\n')])
    print(rline)