import sys

with open(sys.argv[1],'r') as f:
    dance = f.read().strip().split(',')

#seq = list('abcde')
seq = list('abcdefghijklmnop')
Part1 = True
seen = []
times = 1 if Part1 else 1000000000

i = 0
while i < times:
 #  print("Start",''.join(seq))
    for d in dance:
        if d[0] == 's':
            temp = len(seq) - int(d[1:])
            seq = seq[temp : ] + seq[ : temp]
        elif d[0] == 'x':
            x1, x2 = map(int, d[1:].split('/'))
            seq[x1], seq[x2] = seq[x2], seq[x1]
        else:
            x1, x2 = d[1:].split('/')
            i1 = seq.index(x1)
            i2 = seq.index(x2)
            seq[i1], seq[i2] = seq[i2], seq[i1]

    if ''.join(seq) in seen:
        break
    seen.append(''.join(seq))
    i += 1

print(seen[times%i - 1])
