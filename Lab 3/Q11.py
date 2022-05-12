#program to get the file size of a plain file

import os

f = "test1.txt"
size = os.path.getsize(f)
print("The file {} is of size {} bytes".format(f,size))