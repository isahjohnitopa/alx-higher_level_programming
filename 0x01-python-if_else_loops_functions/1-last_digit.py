#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number <= 0:
    numb = -number
else:
    numb = number
if (numb % 10) < 6 and (numb % 10) != 0:
    print(f"Last digit of {number} is {numb % 10} and is less than {6} and not {0}")
elif (numb % 10) > 5:
    print(f"Last digit of {number} is {numb % 10} and is greater than {5}")
else:
    print(f"Last digit of {number} is {numb % 10} and is {0}")
