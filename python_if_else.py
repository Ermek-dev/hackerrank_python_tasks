#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    number = int(input())
    if number%2!=0:
            print("Weird")
    elif number%2==0 and number in range(2,6):
            print("Not Weird")
    elif number%2==0 and number in range(6,21):
            print("Weird")
    elif number%2==0 and number>20:
            print("Not Weird")
    else:
            print("Error")
