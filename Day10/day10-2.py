from functools import reduce
import sys

#basically for part 1 you need to change the length reading
#and only do one iteration of the algorithm
with open(sys.argv[1],'r') as f:
    lengths = [ord(x) for x in f.read().strip()]

lengths += [17, 31, 73, 47, 23]
size = 256
my_list = list(range(0,size))
index = 0
skip_size = 0

for i in range(64):
    for l in lengths:
        #print("Index",index,"skip",skip_size)
        t1 = my_list[index:index+l]
        if index + l> len(my_list):
            #print("First if")
            t2 = my_list[0:(index+l)%len(my_list)]
            #print("t1",t1,"t2",t2)
            t3 = t1 + t2
            t3.reverse()
            #print(t3)
            my_list = t3[len(t1): ] + my_list[(index+l)%len(my_list):index] + t3[0:len(t1)]
        else:
            #print("Second if")
            t1.reverse()
            #print("t1",t1)
            my_list = my_list[0:index] + t1 + my_list[ index + l: ]

        index = (index + l + skip_size)%len(my_list)
        skip_size += 1
        #print(my_list)
        assert(len(my_list)==size)

sparse_hash = my_list
dense_hash = []
for i in range(0,256,16):
    dense_hash.append(reduce((lambda x,y: x^y), sparse_hash[i:i+16]))
print(dense_hash)


knot_hash = ""
for d in dense_hash:
    knot_hash += format(d,'02x')

print(knot_hash)
