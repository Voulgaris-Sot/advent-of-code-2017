#Pretty slow and there are easy improvements. Check out day21_faster.py
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
            lhs2.append(np.array(list(l[0].strip().replace('/',''))).reshape(2,2))
            rhs2.append(np.array(list(l[1].strip().replace('/',''))).reshape(3,3))
        else:
            lhs3.append(np.array(list(l[0].strip().replace('/',''))).reshape(3,3))
            rhs3.append(np.array(list(l[1].strip().replace('/',''))).reshape(4,4))

def test_rotation(x,rule):
    if np.array_equal(x,np.rot90(rule,1)): #1 turn
        return True
    elif np.array_equal(x,np.rot90(rule,2)): #2 turns
        return True
    elif np.array_equal(x,np.rot90(rule,3)): #3 turns
        return True
    return False


def find_next(x, lhs, rhs):
#    print("Searching for")
#    print(x)
    for i, rule in enumerate(lhs):
        found = False
        if (rule == '#').sum() != (x == '#').sum() :
            #skip the rules that definitely dont match
            continue
        if np.array_equal(x,rule) or test_rotation(x,rule):
            found = True
        elif np.array_equal(x,np.flipud(rule)) or test_rotation(x,np.flipud(rule)):
            found = True
        #no need to fliplr or rotate
        if found:
            return rhs[i]
    print("Failed to find match")
    sys.exit()

grid = np.array([['.','#','.'],['.','.','#'],['#','#','#']])
size = grid.shape[0]
Part1 = True
num = 5 if Part1 else 18
for k in range(num):
    print(k)
    if size%2 == 0:
        new_grid = np.empty([size + size//2,size + size//2], dtype = object)
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

print((grid == '#').sum())
