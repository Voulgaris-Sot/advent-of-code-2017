import sys

pos = []
vel = []
acc = []

with open(sys.argv[1],'r') as f:
    for line in f:
        l = line.strip().split(',')
        pos.append([int(l[0].strip("p=<")), int(l[1]), int(l[2].strip(">")) ])
        vel.append([int(l[3].strip(" v=<")), int(l[4]), int(l[5].strip(">")) ])
        acc.append([int(l[6].strip(" a=<")), int(l[7]), int(l[8].strip(">")) ])

for steps in range(0,1000):#1000 is enough
    for p in range(len(pos)):
        for k in range(3):
            vel[p][k] += acc[p][k]
            pos[p][k] += vel[p][k]

x = min(enumerate(pos), key = lambda x: abs(x[1][0]) + abs(x[1][1]) + abs(x[1][2]))
print(x)
