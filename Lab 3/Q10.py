#to count the frequency of words in a file.

from typing import Counter

f = open("test1.txt","r")
txt=f.read()
words=txt.split()
count = Counter(words)
print(count)