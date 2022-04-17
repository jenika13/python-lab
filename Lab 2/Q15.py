#to generate password

import random
import string

maxlen=20
password=''
character=(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation)

for i in range(maxlen):
    password_char=random.choice(character)
    password=password+password_char
print(password)
