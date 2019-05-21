import sys

def my_f(xx):
    x = list(xx)

    mx = max(x)
    index = x.index(mx)
    x[index] = 0
    length = len(x)

    while(mx > 0):
        #move to next position and add one
        index = (index + 1)%length
        x[index] += 1
        mx -= 1
    return x

#from wikipedia
def floyd(f, x0):
    tortoise = f(x0)
    hare = f(f(x0))

    while tortoise != hare:
        tortoise = f(tortoise)
        hare = f(f(hare))

    mu = 0
    tortoise = x0
    while tortoise != hare:
        tortoise = f(tortoise)
        hare = f(hare)   # Hare and tortoise move at same speed
        mu += 1

    # Find the length of the shortest cycle starting from x_μ
    # The hare moves one step at a time while tortoise is still.
    # lam is incremented until λ is found.
    lam = 1
    hare = f(tortoise)
    while tortoise != hare:
        hare = f(hare)
        lam += 1

    return lam, mu

with open(sys.argv[1],'r') as f:
        seq = [int(x) for x in f.read().split()]

#lam = length of the cycle
#lam + mu is the position of the repetition
print(floyd(my_f,seq))

