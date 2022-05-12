#Python program to write a list to a file.

f = open("C:/Users/acer/Desktop/Lab/Python/Lab 3/test1.txt", "w")
l = ["Python","Javascript","C","C#","PHP","Java","C++"]
for i in l:
    f.write(i+"\n")
f.close()
f = open("C:/Users/acer/Desktop/Lab/Python/Lab 3/test1.txt","r")
print(f.read())