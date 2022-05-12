#program to copy the contents of a file to another file .

f = open("C:/Users/acer/Desktop/Lab/Python/Lab 3/test.txt", "r")
g = open("C:/Users/acer/Desktop/Lab/Python/Lab 3/test1.txt", "w")
for items in f:
    g.write(items)
f.close()
g.close()
g = open("C:/Users/acer/Desktop/Lab/Python/Lab 3/test1.txt", "r")
print(g.read())