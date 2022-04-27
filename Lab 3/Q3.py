#to append a file and display it

f = open("C:/Users/acer/Desktop/Lab/Python/Lab 3/test.txt", "a")
f.write("\nObject-Oriented Language.")
f.close()
f = open("C:/Users/acer/Desktop/Lab/Python/Lab 3/test.txt", "r")
print(f.read())
f.close()