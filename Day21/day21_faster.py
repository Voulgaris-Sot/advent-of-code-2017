#It assumes that the input is transformed.
#. -> 0 and # -> 1
#I was too bored to find a way around it or transform myself
#Just do it in the editor. in100.txt and in200.txt are in that form
#also really messy solution for the production of flips and rotations of a rule
import sys
import numpy as np

lhs2 = []
lhs3 = []
rhs2 = []
rhs3 = []

with open(sys.argv[1],'r') as f:
    for l in f:
        l = l.split('=>')
        if len(l[0].strip()) == 5:
            lhs2.append(np.array(list(l[0].strip().replace('/','')), dtype = int).reshape(2,2))
            rhs2.append(np.array(list(l[1].strip().replace('/','')), dtype = int).reshape(3,3))
        else:
            lhs3.append(np.array(list(l[0].strip().replace('/','')), dtype = int).reshape(3,3))
            rhs3.append(np.array(list(l[1].strip().replace('/','')), dtype = int).reshape(4,4))

def test_rotation(x,rule):
    if np.array_equal(x,np.rot90(rule,1)): #1 turn
        return True
    elif np.array_equal(x,np.rot90(rule,2)): #2 turns
        return True
    elif np.array_equal(x,np.rot90(rule,3)): #3 turns
        return True
    return False

#really messy
lh2Transform = []
lh3Transform = []
for i,rule in enumerate(lhs2):
    lh2Transform.append([])
    lh2Transform[i].append(rule)
    lh2Transform[i].append(np.rot90(rule,1))
    lh2Transform[i].append(np.rot90(rule,2))
    lh2Transform[i].append(np.rot90(rule,3))
    rule = np.flipud(rule)
    lh2Transform[i].append(rule)
    lh2Transform[i].append(np.rot90(rule,1))
    lh2Transform[i].append(np.rot90(rule,2))
    lh2Transform[i].append(np.rot90(rule,3))
for i,rule in enumerate(lhs3):
    lh3Transform.append([])
    lh3Transform[i].append(rule)
    lh3Transform[i].append(np.rot90(rule,1))
    lh3Transform[i].append(np.rot90(rule,2))
    lh3Transform[i].append(np.rot90(rule,3))
    rule = np.flipud(rule)
    lh3Transform[i].append(rule)
    lh3Transform[i].append(np.rot90(rule,1))
    lh3Transform[i].append(np.rot90(rule,2))
    lh3Transform[i].append(np.rot90(rule,3))

def find_next(x, lhs, rhs):
#    print("Searching for")
#    print(x)
    for i, rule in enumerate(lhs):
        found = False
        if np.sum(rule) != np.sum(x):
            #skip the rules that definitely dont match
            continue
        if x.size == 4:
            for t in lh2Transform[i]:
                if np.array_equal(x,t):
                    return  rhs[i]
        else:
            for t in lh3Transform[i]:
                if np.array_equal(x,t):
                    return  rhs[i]
    print("Failed to find match")
    sys.exit()

grid = np.array([[0,1,0],[0,0,1],[1,1,1]])
size = grid.shape[0]
Part1 = False
num = 5 if Part1 else 18
for k in range(num):
    print(k)
    if size%2 == 0:
        new_grid = np.empty([size + size//2,size + size//2], dtype = int)
        new_i = 0
        for i in range(0,size,2):
            new_j = 0
            for j in range(0,size,2):
                square = grid[i:i+2,j:j+2]
                new_grid[new_i:new_i+3, new_j:new_j+3] = find_next(square, lhs2, rhs2)
                new_j += 3
            new_i += 3
        size += size//2
    else:
        new_grid = np.empty([size + size//3,size + size//3], dtype=object)
        new_i = 0
        for i in range(0,size,3):
            new_j = 0
            for j in range(0,size,3):
                square = grid[i:i+3,j:j+3]
                new_grid[new_i:new_i+4, new_j:new_j+4] = find_next(square, lhs3, rhs3)
                new_j += 4
            new_i += 4
        size += size//3
    grid = new_grid

print(np.sum(grid))
