#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
greater = "and is greater than 5"
less = "and is less than 6 and not 0"
is_zero = "and is 0"
if number % 10 == 0:
    print(f"Last digit of {number} is {number % 10} {is_zero}")
elif number % 10 > 5:
    print(f"Last digit of {number} is {number % 10} {greater}")
else:
    print(f"Last digit of {number} is {number % 10} {less}")
