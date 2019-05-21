#I have no idea if part 2 works for leaf node
import sys
from collections import defaultdict

name = []
weight = {}
children = {}

with open(sys.argv[1],'r') as f:
    for line in f:
        tower = line.split()
        name.append(tower[0])
        weight[tower[0]] = (int( tower[1].replace('(',''). replace(')','') ) )
        if len(tower) > 2 :
            children[tower[0]] = [ x.replace(',','') for x in tower[3:] ]
        else:
            children[tower[0]] = []
            pseudo_top = tower[0]

#start from a leaf and make your way down to the root
while(True):
    found = False
    for n in name:
        if pseudo_top in children[n]:
            pseudo_top = n
            found = True
            break
    if not found:
        print("Answer1:",pseudo_top)
        break

###PART 2
##First a dfs to find the weights
root = pseudo_top
discovered = []
holding_weight = defaultdict(list)
children_weight = defaultdict(list)

def dfs(v):
    discovered.append(v)
    temp = []
    if not children[v]:
        holding_weight[v] = weight[v]
        return
    for x in children[v]:
        if x not in discovered:
            dfs(x)
        children_weight[v].append(holding_weight[x])
    holding_weight[v] = sum(children_weight[v]) + weight[v]

dfs(root)
v = root

#Start from the root and inspect the children to find the one
#that is unique. If you can't find a unique one then you found
#the node you need to change.
while(True):
    #print("Node:", v)
    #print("Children Weight", t[v])
    #print("Children", children[v])
    unique = False
    for i,x in enumerate(children_weight[v]):
        if children_weight[v].count(x) == 1:
            unique = True
            previous_weights = children_weight[v]
            v = children[v][i]
            break

    #if all the children have the same weights
    if not unique:
        print("Answer 2")
        print("The problematic node is:", v)
        print("It's current weight is:", weight[v])
        print("And the previous weights are:", previous_weights)
        print("So just do the math:")
        break
