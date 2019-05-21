import sys
from collections import defaultdict

name = []
children = {}

with open(sys.argv[1],'r') as f:
    for line in f:
        l = line.split()
        name.append(l[0])
        children[l[0]] = [ x.replace(',','') for x in l[2:] ]

#print(name,children)

def dfs(v):
    discovered.append(v)
    if not children[v]:
        return
    for x in children[v]:
        if x not in discovered:
            dfs(x)

discovered = []
###PART 1
dfs('0')
print("Part 1",len(discovered))

###PART 2
count = 1 #1 because already dfs from 0
for n in name:
    if n not in discovered:
        dfs(n)
        count += 1
print("Part 2",count)
print(len(discovered))
print(len(name))
