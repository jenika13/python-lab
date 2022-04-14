#to calculate repeated characters in a string

str = input("Enter a string : ")

dictionary = {}
rep={}

for a in str:
        dictionary[a]=dictionary.get(a,0)+1
for a in dictionary:
    if dictionary[a]>1:
        rep[a]=dictionary[a]
print("The repeated characters are \n{} ".format(rep))