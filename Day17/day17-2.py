my_input = 371

i = 0
seq = [0]
for length in range(1,50000001):
    i = (i + my_input) % length + 1
    #seq.insert(i,ii)
    #print(seq)
    if i == 1:
        answer = length

print(answer)
