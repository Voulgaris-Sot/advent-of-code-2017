w#silly bruteforce idea
import sys

with open(sys.argv[1],'r') as f:
        seq = [int(x) for x in f.read().split()]

length = len(seq)
all_seqs = []
print(seq)

for i in range(50000):#again arbitrary number
    mx = max(seq)
    index = seq.index(mx)
    seq[index] = 0

    while(mx > 0):
        #move to next position and add one
        index = (index + 1)%length
        seq[index] += 1
        mx -= 1
    #all_seqs.append(list(seq))
    print(seq)
    if seq not in all_seqs:
        all_seqs.append(list(seq))
    else:
        print("HEY",seq,i+1)
        break

#print(all_seqs)
