import sys

with open(sys.argv[1],'r') as f:
        stream = f.read().strip()
        #print(stream)

group_val = 0
garbage = False
skip= False
q1 = 0
q2 = 0

for c in stream:
    if skip:
        skip = False
        continue

    if c == '!':
        skip = True
        continue

    if garbage:
        if c == '>':
            garbage = False
        else:
            q2 += 1
            continue

    if c == '<':
        garbage = True

    if c == '{':
        group_val += 1

    if c == '}':
        q1 += group_val
        group_val -= 1

print(q1)
print(q2)
