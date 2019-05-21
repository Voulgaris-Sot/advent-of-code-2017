my_input = 371

i = 0
seq = [0]
for length in range(1,2018):
    i = (i + my_input) % length + 1
    seq.insert(i, length)

print(seq[seq.index(2017)+1])
