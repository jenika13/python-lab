a = str(input("Enter a string : "))
def reverse(string):
    string=string[::-1]
    return string
b=reverse(a)
if (a.lower()==b.lower()):
    print("The given string is palindrome.")
else:
    print("The given string is not a palindrome.")