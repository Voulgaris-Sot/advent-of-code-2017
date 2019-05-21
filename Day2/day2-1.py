import sys

def process_line(seq):
    return max(seq)-min(seq)

my_sum = 0

with open(sys.argv[1],'r') as f:
    for line in f:
        seq = [int(x) for x in line.split()]
        my_sum += process_line(seq)

print(my_sum)
