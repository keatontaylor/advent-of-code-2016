import sys
import math

with open('advent2.txt') as f:
    lines = f.readlines()


x = 0
y = 0

 
for line in lines:

    for i in line:
        if i == 'U':
            if  y != 1:
                y = y + 1
        elif i == 'R':
            if x != 1: 
                x = x + 1
        elif i == 'L':
            if x != -1:
                x = x - 1
        elif i == 'D':
            if y != -1:
                y = y - 1
            
    print '({0},{1})'.format(x,y)
    
