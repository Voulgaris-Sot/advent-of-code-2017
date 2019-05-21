import sys
import copy
from collections import defaultdict

ports = []
with open(sys.argv[1],'r') as f:
    for i,l in enumerate(f):
        ports.append(list(map(int,l.strip().split('/'))))
        if l.strip().split('/')[0] == '0':
            #assume that 0 is in the first place
            start = i

ports_used = [[False,False] for i in range(len(ports))]
children = defaultdict(list)
cost = [sum(p) for p in ports]
for i in range(len((ports))):
    for j in range(len(ports)):
        if i==j:
            continue
        if ports[i][0] == ports[j][0]:
            children[i].append([j,0,0])
        if ports[i][1] == ports[j][0]:
            children[i].append([j,1,0])
        if ports[i][0] == ports[j][1]:
            children[i].append([j,0,1])
        if ports[i][1] == ports[j][1]:
            children[i].append([j,1,1])
ans1 = -1
ans2_length = -1
ans2_strength = -1
def explore(v,path,s,used):
    global ans1, ans2_length, ans2_strength
    path.append(v)
    s += cost[v]

    if s > ans1:
        #I could only check in deadend.
        ans1 = s

    if len(path) > ans2_length and ans2_strength < s:
        ans2_length = len(path)
        ans2_strength = s

    if not children[v]:
        print("Should not happen",s)
        return

    for x in children[v]:
        #x[0] pou paei
        #x[1] port pou ksekinaei
        #x[2] port poy kataligei
        if used[v][x[1]]:
 #           print("Tried to acces my used port",v,x[1])
            continue
        if used[x[0]][x[2]]:
 #           print("Tried to acces other used port",x[0],x[1])
            continue
        used[v][x[1]] = True
        used[x[0]][x[2]] = True
        explore(x[0],path.copy(),s, used.copy())
        used[v][x[1]] = False
        used[x[0]][x[2]] = False

ports_used[start][0] = True
explore(start, [], 0, ports_used)
print(ans1)
print(ans2_length, ans2_strength)

