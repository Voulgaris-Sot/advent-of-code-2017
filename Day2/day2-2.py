import sys

def process_line(seq):
    seq.sort()
    #print(seq)
    length = len(seq)
    for i in range(length):
        for ii in range(i+1,length):
            if seq[ii]%seq[i] == 0:
                print(i,ii)
                return seq[ii]//seq[i]


my_sum = 0

with open(sys.argv[1],'r') as f:
    for line in f:
        seq = [int(x) for x in line.split()]
        my_sum += process_line(seq)

print(my_sum)
