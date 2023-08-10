#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
x = number
if number <= 0:
    y = -x
    if (y % 10) != 0:
        print(f"Last digit of {x} is {-(y % 10)} and is less than 6 and not 0")
    else:
        print(f"Last digit of {x} is {y % 10} and is {0}")
else:
    if (x % 10) < 6 and (x % 10) != 0:
        print(f"Last digit of {x} is {x % 10} and is less than 6 and not 0")
    elif (x % 10) > 5:
        print(f"Last digit of {x} is {x % 10} and is greater than 5")
    else:
        print(f"Last digit of {x} is {x % 10} and is 0")
