from collections import defaultdict
from functools import reduce
import sys

#python3-like way '{:0128b}'.format(int(v, 16))'
def hex2bin(string):
    bin = ['0000','0001','0010','0011',
            '0100','0101','0110','0111',
            '1000','1001','1010','1011',
            '1100','1101','1110','1111']
    aa = ''
    for i in range(len(string)):
        aa += bin[int(string[i],base=16)]
    return aa

def knot_hash(my_key):
    size = 256
    my_list = list(range(0,size))

    lengths = [ord(x) for x in my_key]
    lengths += [17, 31, 73, 47, 23]

    index = 0
    skip_size = 0

    for i in range(64):
        for l in lengths:
            t1 = my_list[index:index+l]
            if index + l> len(my_list):
                t2 = my_list[0:(index+l)%len(my_list)]
                t3 = t1 + t2
                t3.reverse()
                my_list = t3[len(t1): ] + my_list[(index+l)%len(my_list):index] + t3[0:len(t1)]
            else:
                t1.reverse()
                my_list = my_list[0:index] + t1 + my_list[ index + l: ]
            index = (index + l + skip_size)%len(my_list)
            skip_size += 1
            assert(len(my_list)==size)

    sparse_hash = my_list
    dense_hash = []
    for i in range(0,256,16):
        dense_hash.append(reduce((lambda x,y: x^y), sparse_hash[i:i+16]))

    knot_hash = ""
    for d in dense_hash:
        knot_hash += format(d,'02x')
    return knot_hash


with open(sys.argv[1],'r') as f:
    key = f.read().strip()

grid = []
#key = "flqrgnkx"
for i in range(128):
    to_hash = key + '-' + str(i)
    hashed = knot_hash(to_hash)
    grid.append(hex2bin(hashed))

#Part 1
#count = 0
#for line in grid:
#    count += line.count("1")
#print(count)

#Part 2
def to_name(i,j):
    return "{:03d}|{:03d}".format(i,j)

nodes = []
graph = defaultdict(list)
for i in range(128):
    for j in range(128):
        if grid[i][j] == "0":
            continue
        nodes.append(to_name(i,j))
        #no loop around
        if i>0 and grid[i-1][j] == "1":
            graph[to_name(i,j)].append(to_name(i-1,j))
        if i<127 and  grid[i+1][j] == "1":
            graph[to_name(i,j)].append(to_name((i+1),j))
        if j>0 and grid[i][j-1] == "1":
            graph[to_name(i,j)].append(to_name(i,j-1))
        if j<127 and grid[i][(j+1)%128] == "1":
            graph[to_name(i,j)].append(to_name(i,(j+1)))

#print(nodes)
def dfs(v):
    discovered.append(v)
    if not graph[v]:
        return
    for x in graph[v]:
        if x not in discovered:
            dfs(x)

discovered = []
count2 = 0
for n in nodes:
    if n not in discovered:
        dfs(n)
        count2 += 1
print("Part 2",count2)
