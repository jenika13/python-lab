#to count the number of lines in a text file.

f = open("test1.txt","r")
lines = f.readlines()
count = 0
for i in lines:
    count=count+1
print(count)