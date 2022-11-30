#!/usr/bin/python3
#Import random numbers#
import random
number = random.randint(-10000, 10000)
#write a program that will detect print the the last digit of a random number#
#codition1: If greater than 5
#condition2: If the number is 0#
#condition3: If the number is less than 6 and not 0#
print(f"Last digit of {number} is {number}", end="\n")
if (number > 5):
    print("and is greater than 5")
    print(end="\n")
elif (number == 0):
    print("and is 0")
    print(end="\n")
elif (number < 6 and not 0):
    print("and is less than 6 and not 0")
