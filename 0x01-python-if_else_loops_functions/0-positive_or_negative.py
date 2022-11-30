#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if(number > 0):
    print("98 is positive", end="\n")
elif(number == 0):
    print("0 is zero", end="\n")
elif(number < 0):
    print("-98 is negative", end="\n")
