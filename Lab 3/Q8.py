#program to find the longest words.

f = open("test1.txt","r")
txt = f.read()
words = txt.split()
max_len = len(max(words, key=len))
for item in words:
    if len(item)==max_len:
        print(item)