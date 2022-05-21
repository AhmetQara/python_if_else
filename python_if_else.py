#!/bin/python3

import math
import os
import random
import re
import sys

def weird_num(n):
    
    if n % 2 == 1:
        print("Weird")
        
    if n < 5 and n >= 2 and n % 2 == 0: 
        print("Not Weird")
        
    if  n <= 20 and n >= 6 and n % 2 == 0:
        print("Weird")
        
    if  n > 20 and n % 2 == 0:
        print("Not Weird")

if __name__ == '__main__':
    n = int(input().strip())

weird_num(n)
