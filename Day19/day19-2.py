import sys
import numpy as np

with open(sys.argv[1],'r') as f:
        grid = [line.strip('\n') for line in f]

posx = 0
posy = grid[0].find('|')#first position
direction = "down"
final = "LXWCKGRAOY" #"ABCDEF"
answer = ""
steps = 1
Done = False

while not Done:
    if direction == "down":
        while True:
            steps += 1
            posx += 1
            if grid[posx][posy] == '+':
                if posy>0 and (grid[posx][posy-1]=='-' or grid[posx-1][posy].isalpha()):
                    direction = "left"
                else:
                    direction = "right"
                break
            if grid[posx][posy].isalpha():
                answer += grid[posx][posy]
                if answer == final:
                    Done=True
                    break
    elif direction == "up":
        while True:
            steps += 1
            posx -= 1
            if grid[posx][posy] == '+':
                if posy>0 and (grid[posx][posy-1]=='-' or grid[posx-1][posy].isalpha()):
                    direction = "left"
                else:
                    direction = "right"
                break
            if grid[posx][posy].isalpha():
                answer += grid[posx][posy]
                if answer == final:
                   Done = True
                   break
    elif direction == "left":
        while True:
            steps += 1
            posy -= 1
            if grid[posx][posy] == '+':
                if posx>0 and (grid[posx-1][posy]=='|' or grid[posx-1][posy].isalpha()):
                    direction = "up"
                else:
                    direction = "down"
                break
            if grid[posx][posy].isalpha():
                answer += grid[posx][posy]
                if answer == final:
                   Done = True
                   break
    elif direction == "right":
        while True:
            steps += 1
            posy += 1
            if grid[posx][posy] == '+':
                if posx>0 and (grid[posx-1][posy]=='|' or grid[posx-1][posy].isalpha()):
                    direction = "up"
                else:
                    direction = "down"
                break
            if grid[posx][posy].isalpha():
                answer += grid[posx][posy]
                if answer == final:
                   Done = True
                   break

print(posx,posy,steps)
