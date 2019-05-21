#pretty slow. Could find periods and determine it from there
#directly or at least help you search
import sys

name = []
layers = {}

with open(sys.argv[1],'r') as f:
    for line in f:
        l = line.strip().split(': ')
        layers[int(l[0])] = int(l[1])

delay = 0
while True:
    caught = False
    for i in range(max(layers) + 1):
        if i not in layers:
            continue
        time = delay + i
        if (time//(layers[i]-1))%2 == 0:
            pos = time%(layers[i] - 1)
        else:
            pos = layers[i] - 1 - time%(layers[i]-1)
        if pos == 0:
            #print(i)
            caught = True
            break
    if not caught:
        print("Delay:",delay)
        break
    delay += 1

