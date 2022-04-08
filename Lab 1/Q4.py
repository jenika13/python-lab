num=int(input("Enter a number : "))
print("The divisors of the given number are given below")
for i in range(1,num+1):
    if (num%i==0):
        print(i)