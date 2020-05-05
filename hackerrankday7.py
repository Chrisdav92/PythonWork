import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    my_str = ""
    arr = list(map(str, input().rstrip().split()))

    arr.reverse()
    for x in arr:
       my_str = my_str + x + " "
    print(my_str)