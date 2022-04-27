#to read a file line by line store it into an array.

f = open("C:/Users/acer/Desktop/Lab/Python/Lab 3/test.txt", "r")
arr=[]
for i in f:
    arr.append(i)
print(arr)
f.close()