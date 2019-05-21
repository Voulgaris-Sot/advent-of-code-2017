import sys

#Pretty simple. If the list is longer than the set, then repeated phrase

def process_line(seq):
    return len(seq) == len(set(seq))

my_sum = 0

with open(sys.argv[1],'r') as f:
    for line in f:
        seq = line.split()
        #print(seq)
        my_sum += process_line(seq)

print(my_sum)
