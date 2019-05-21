#without sort and with itertools combinations to loop through all
#combinations in a line

import itertools
import sys

lines = []
with open(sys.argv[1],'r') as f:
    for line in f:
        lines.append( [int(x) for x in line.split()] )

part1 = 0
part2 = 0
for line in lines:
    part1 += max(line) - min(line)

    for i in itertools.combinations(line, 2):
        print i
        if max(i) % min(i) == 0:
            part2 += max(i) / min(i)
            break

