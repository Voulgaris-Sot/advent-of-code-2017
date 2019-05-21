import sys
import numpy as np
from collections import Counter
with open(sys.argv[1],'r') as f:
        grid = [line.strip('\n') for line in f]

#def f(x):
#    return x.isalpha()
#print(sum(list(map(f, (c for g in grid for c in g)))))
answer_len = sum(c.isalpha() for s in grid for c in s)

posx = 0
posy = grid[0].find('|')#first position
direction = "down"
answer = ""
Done = False

while not Done:
    #print(posx,posy,direction)
    if direction == "down":
        while True:
            posx += 1
            if grid[posx][posy] == '+':
                if posy>0 and (grid[posx][posy-1]=='-' or grid[posx-1][posy].isalpha()):
                    direction = "left"
                else:
                    direction = "right"
                break
            if grid[posx][posy].isalpha():
                answer += grid[posx][posy]
                if len(answer) == answer_len:
                    Done = True
                    break
    elif direction == "up":
        while True:
            posx -= 1
            if grid[posx][posy] == '+':
                if posy>0 and (grid[posx][posy-1]=='-' or grid[posx-1][posy].isalpha()):
                    direction = "left"
                else:
                    direction = "right"
                break
            if grid[posx][posy].isalpha():
                answer += grid[posx][posy]
                if len(answer) == answer_len:
                    Done = True
                    break
    elif direction == "left":
        while True:
            posy -= 1
            if grid[posx][posy] == '+':
                if posx>0 and (grid[posx-1][posy]=='|' or grid[posx-1][posy].isalpha()):
                    direction = "up"
                else:
                    direction = "down"
                break
            if grid[posx][posy].isalpha():
                answer += grid[posx][posy]
                if len(answer) == answer_len:
                    Done = True
                    break
    elif direction == "right":
        while True:
            posy += 1
            if grid[posx][posy] == '+':
                if posx>0 and (grid[posx-1][posy]=='|' or grid[posx-1][posy].isalpha()):
                    direction = "up"
                else:
                    direction = "down"
                break
            if grid[posx][posy].isalpha():
                answer += grid[posx][posy]
                if len(answer) == answer_len:
                    Done = True
                    break
print(posx,posy,answer)
