#Python program to read a random line from a file.

import random

f = open("C:/Users/acer/Desktop/Lab/Python/Lab 3/test.txt", "r")
lines = f.readlines()
rand = random.choice(lines)
print(rand)