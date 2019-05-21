import sys

#The only difference is that I sort each phrase of the passphrase

def process_line(seq):
    return len(seq) == len(set(seq))

my_sum = 0

with open(sys.argv[1],'r') as f:
    for line in f:
        seq = [''.join(sorted(x)) for x in line.split()]
        #print(seq)
        my_sum += process_line(seq)

print(my_sum)
