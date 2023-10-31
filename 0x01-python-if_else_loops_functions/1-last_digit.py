#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last_digit = abs(number) % 10

output = f"Last digit of {number}  is {last_digit}"
if number < 0:
    last_d = last_digit * -1
    if (last_digit == 0):
        print(f"Last digit of {number}  is {last_d} and is 0")
    else:
        print(f"Last digit of {number}  is {last_d} and is less than 6 and not 0")
else:
    if (last_digit > 5):
        print(output + " and is greater than 5")
    elif (last_digit == 0):
        print(output + " and is 0")
    else:
        print(output + " and is less than 6 and not 0")
