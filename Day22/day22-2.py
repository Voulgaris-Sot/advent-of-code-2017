import sys
import numpy as np

with open(sys.argv[1],'r') as f:
    grid = np.array([list(line.strip('\n')) for line in f])

turn_right = {'up':'right', 'left':'up', 'down': 'left', 'right' : 'down' }
turn_left  = {'up':'left', 'left':'down', 'down': 'right', 'right' : 'up' }
turn_around  = {'up':'down', 'left':'right', 'down': 'up', 'right' : 'left' }

currentX = grid.shape[0]//2
currentY = grid.shape[1]//2
direction = "up"

clean = '.'
infected = '#'
weakened = 'W'
flagged = 'F'

bursts = 10000000
ans = 0
for i in range(bursts):
    #First check to see if we need to add new rows
    if currentX < 0:
        grid = np.insert(grid,0,'.',axis = 0) #insert up
        currentX = 0
    elif  currentX >= grid.shape[0]:
        grid = np.insert(grid,grid.shape[0],'.',axis = 0) #insert down
        currentX = grid.shape[0] - 1
    elif currentY < 0:
        grid = np.insert(grid,0,'.',axis = 1) #inser left
        currentY = 0
    elif  currentY >= grid.shape[1]:
        grid = np.insert(grid,grid.shape[1],'.',axis = 1) #insert right
        currentY = grid.shape[1] - 1

    #rules of the automaton
    if grid[currentX][currentY] == infected:
        direction = turn_right[direction]
        grid[currentX][currentY] = flagged
    elif grid[currentX][currentY] == clean:
        direction = turn_left[direction]
        grid[currentX][currentY] = weakened
    elif grid[currentX][currentY] == flagged:
        direction = turn_around[direction]
        grid[currentX][currentY] = clean
    elif grid[currentX][currentY] == weakened:
        #no change in direction
        grid[currentX][currentY] = infected
        ans += 1

    #move forward
    if direction == 'up':
        currentX -= 1
    elif direction == 'down':
        currentX += 1
    elif direction == 'right':
        currentY += 1
    else:
        currentY -= 1
print(ans)
