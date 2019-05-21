import sys

with open(sys.argv[1],'r') as f:
    seq = [int(x) for line in f for x in line.split()]


i=0 #pos on the list
length = len(seq)
steps = 0

while(i<length and i>=0):
    if seq[i] >=3:
        seq[i] += -1
        i += seq[i] + 1
    else:
        seq[i] += 1
        i += seq[i] - 1
    steps += 1

print(steps)
