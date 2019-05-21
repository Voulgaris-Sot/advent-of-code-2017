import sys

with open(sys.argv[1],'r') as f:
    seq = [int(s) for s in f.read().strip()]

#print(seq)
my_sum = 0

length = len(seq)
dist = length//2

for i in range(length):
    if seq[i] == seq[(i+dist)%length]:
        my_sum += seq[i]

print(my_sum)
