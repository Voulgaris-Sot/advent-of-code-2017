seedA = 703#65
seedB = 516#89216

def nextA(x):
    return (x*16807)%2147483647

def nextB(x):
    return (x*48271)%2147483647

A = seedA
B = seedB
count = 0
Part1 = True
times = 40000000 if Part1 else 5000000
for i in range(times):
    while True:
        A = nextA(A)
        if A%4 == 0 or Part1:
            break
    while True:
        B = nextB(B)
        if B%8 == 0 or Part1:
            break
    if A&65535 == B&65535:
        count+=1
    #print(A,B)
print(count)
