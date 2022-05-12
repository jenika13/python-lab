#Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0).

#using recursive function

def sum_pos_int(x):
    if x<=0:
        return 0
    else:
        return (x + sum_pos_int(x-2))

n = int(input("Enter a positive integer : "))
print(sum_pos_int(n))