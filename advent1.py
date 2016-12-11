import csv
import math

f = open('input.txt', 'r')

reader = csv.reader(f, skipinitialspace=True,delimiter=',', quoting=csv.QUOTE_NONE)


coords = list(reader)

facing = 'N'
x = 0
y = 0

for coord in coords[0]:
    direction = coord[:1]
    value = coord[1:]

    if facing == 'N':
        if direction == 'R':
            facing = 'E'
            x = x + int(value)
          
        elif direction == 'L':
            facing = 'W'
            x = x - int(value)

    elif facing == 'E':
        if direction == 'R':
            facing = 'S'
            y = y - int(value)

        elif direction == 'L':
            facing = 'N'
            y = y + int(value)

    elif facing == 'S':
        if direction == 'R':
            facing = 'W'
            x = x - int(value)

        elif direction == 'L':
            facing = 'E'
            x = x + int(value)

    elif facing == 'W':
        if direction == 'R':
            facing = 'N'
            y = y + int(value)

        elif direction == 'L':
            facing = 'S'
            y = y - int(value)

    
print 'Easter Bunny HQ is {0} blocks away'.format(abs(x) + abs(y))

