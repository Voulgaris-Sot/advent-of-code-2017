# \     1    /
# \       0/
# 1\ -1   /   0
# -1\____/       1
#0  / X  \ -1
#--/    Z \_______
# 0\ Y    /  -1
# -1\____/      1
#1  / -1 \0
#  /    0 \
# / 1      \
#https://www.redblobgames.com/grids/hexagons/#distances
import sys

with open(sys.argv[1],'r') as f:
    directions = f.read().strip().split(',')

#print(directions)
x = y = z = 0
answer2 = -1
for d in directions:
    if d == 'n':
        x += 1
        y -= 1
    elif d == 's':
        y += 1
        x -= 1
    elif d == 'nw':
        x += 1
        z -= 1
    elif d == 'sw':
        y += 1
        z -= 1
    elif d == 'ne':
        y -= 1
        z += 1
    elif d == 'se':
        x -= 1
        z += 1
    if max(abs(x),abs(y),abs(z)) > answer2:
        answer2 = max(abs(x),abs(y),abs(z))

print("Part 1:",max(abs(x),abs(y),abs(z)))
print("Part 2:",answer2)
