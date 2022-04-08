import random
num=random.randrange(1,10)
guess=int(input("Guess a number from 1-9 : "))
if guess not in range(1,10):
    print("You must guess a number from 1-9")
elif guess>num:
    print("You guessed a higher number.")
elif guess<num:
    print("You guessed a lower number.")
elif guess==num:
    print("You guessed the exact number.")