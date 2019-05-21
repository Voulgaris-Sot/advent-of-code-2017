import numpy as np
import sys

yy = np.zeros(shape=(101,101), dtype=np.uint64)#lets say 101 is enough
middle = 50

#set up initial square to make our live easier
yy[middle,middle] = 1
yy[middle    ,middle + 1] = 1
yy[middle - 1,middle + 1] = 2
yy[middle - 1,middle    ] = 4
yy[middle - 1,middle - 1] = 5
yy[middle    ,middle - 1] = 10
yy[middle + 1,middle - 1] = 11
yy[middle + 1,middle    ] = 23
yy[middle + 1,middle + 1] = 25

pos_x = middle + 1
pos_y = middle + 2
no_steps = 4 #no_steps to take in each direction
puzzle_in = 361527

for i in range(30):#arbitrary 30
    #first we move up
    for ii in range(no_steps - 1):
        #+1 on the end position to include it
        yy[pos_x , pos_y] = np.sum(yy[pos_x-1:pos_x+1 + 1, pos_y-1: pos_y+1 + 1])

        if yy[pos_x, pos_y] > puzzle_in:
            print(yy[pos_x, pos_y])
            sys.exit()

        pos_x -= 1
    #then left
    for ii in range(no_steps):
        yy[pos_x , pos_y] = np.sum(yy[pos_x-1:pos_x+1 + 1, pos_y-1: pos_y+1 + 1])

        if yy[pos_x, pos_y] > puzzle_in:
            print(yy[pos_x, pos_y])
            sys.exit()

        pos_y -= 1
    #then down
    for ii in range(no_steps):
        yy[pos_x , pos_y] = np.sum(yy[pos_x-1:pos_x+1 + 1, pos_y-1: pos_y+1 + 1])

        if yy[pos_x, pos_y] > puzzle_in:
            print(yy[pos_x, pos_y])
            sys.exit()

        pos_x += 1
    #then right
    for ii in range(no_steps + 1):
        yy[pos_x , pos_y] = np.sum(yy[pos_x-1:pos_x+1 + 1, pos_y-1: pos_y+1 + 1])
        if yy[pos_x, pos_y] > puzzle_in:
            print(yy[pos_x, pos_y])
            sys.exit()
        pos_y += 1

    no_steps += 2
#np.set_printoptions(precision=2, suppress=True, linewidth=120)
#print(yy)
