#program to combine each line from first file with the corresponding line in second file.

f = open("C:/Users/acer/Desktop/Lab/Python/Lab 3/test.txt","r")
g = open("C:/Users/acer/Desktop/Lab/Python/Lab 3/test1.txt","r")
f1 = f.readlines()
g1 = g.readlines()
for i in range(len(f1)):
    merge=g1[i]+f1[i]
    print(merge)