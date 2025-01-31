#!/usr/bin/env python3

#Author: Tommy Long
#Author ID: TLONG10
#Date Created: 2024/01/31

import sys

if len(sys.argv) == 2:   #Checks if exactly 1 argument is provided, fails 0 and 2+ arguments
    timer = int(sys.argv[1])
else:
    timer= 3    #assigns value of 3 when the previous check fails

while timer != 0: #Repeating while loop til 0
    print(timer)
    timer = timer - 1

print('blast off!')
