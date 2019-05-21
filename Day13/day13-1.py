import sys

name = []
layers = {}

with open(sys.argv[1],'r') as f:
    for line in f:
        l = line.strip().split(': ')
        layers[int(l[0])] = int(l[1])

count = 0

for i in range(max(layers) + 1):
    if i not in layers:
        continue
    pos = 0
        
    if (i//(layers[i]-1))%2 == 0:
        pos = i%(layers[i] - 1)
    else:
        pos = layers[i] - 1 - i%(layers[i]-1)
    #for ii in range(i):
    #    if pos == layers[i] - 1:
    #        step = -1
    #    if pos == 0:
    #        step = 1
    #    pos += step
    if pos == 0:
        print("Collision at:",i)
        count += i*layers[i]

print(count)
