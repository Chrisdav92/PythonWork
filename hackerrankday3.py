#-------------------------------Challenge 1--------------------------------------------
"""
# Declare second integer, double, and String variables.
i = 4
d = 4.0
s = 'HackerRank '
# Read and save an integer, double, and String to your variables.
number = input("input a number: ")
double = input("input a double: ")
string = input("put a string: ")
# Print the sum of both integer variables on a new line.

print(i+number)
# Print the sum of the double variables on a new line.
print(d+double)
# Concatenate and print the String variables on a new line
print(s+ string)
# The 's' variable above should be printed first.

"""
#-------------------------------Challenge 2--------------------------------------------
"""
import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):

    if __name__ == '__main__':
        meal_cost = float(input())
        tip_percent = int(input())
        tax_percent = int(input())

        tip = meal_cost*(tip_percent/100)
        tax = meal_cost*(tax_percent/100)
        total_cost = meal_cost + float(tip + tax)
        print(round(total_cost))
"""
#-------------------------------Challenge 3--------------------------------------------
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

if n%2 == 0:
    if 2<= n <=5:
        print("Not Weird")
    elif 6<=n<=20:
        print("Weird")   
    else:
        print("Not Weird")
else:
    print("Weird")