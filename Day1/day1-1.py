#see day1-2 for a cleaner version
import sys

with open(sys.argv[1],'r') as f:
    seq = f.read().strip()

#circular list
seq += seq[0]

print(seq)
prev = ""
my_sum = 0

for s in seq:
    if s == prev:
        my_sum += int(s)
    prev = s

print(my_sum)
