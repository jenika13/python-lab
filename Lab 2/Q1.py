#to create all possible strings by using 'a', 'e', 'i', 'o', 'u'

import random

vowels = ['a','e','i','o','u']

for i in vowels:
    random.shuffle(vowels)
    print("".join(vowels))