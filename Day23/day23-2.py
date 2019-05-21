import math

#stolen from somewhere
def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

b = 108100
c = 125100
cnt = 0
total = 0
while b!= c:
    if is_prime(b):
        cnt += 1
    b += 17
    total += 1

print(total + 1 - cnt)
