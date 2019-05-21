from math import *
import sys

#does not work for n<=3
n = int(sys.argv[1])

#Find the square base that contains n
for base in range(1,n,2):
    if base >= ceil(sqrt(n)):
        break

#the guide is a corner from which we will start to add/substract 1
guide = base**2

#go around to the closet corner of the square
while(n <= guide - base):
    guide = guide - base + 1

#print("N:",n)
#print("Base:",base)
#print("Guide:",guide)

answer = base - 1

#Move closer to n.Either stay on corner or go to the middle
if n > guide - ceil(base/2):
    #If we stay on a corner, substract 1
    step = -1
    guide2 = guide
    answer2 = answer
else:
    #If we end up in the middle, add 1
    step = 1
    guide2 = guide - ceil(base/2)
    answer2 = answer -  ceil((base-2)/2) + 1

for x in range(guide2, guide2 - ceil(base/2), -1):
    if x == n:
        print("Method 1",answer2)
        break
    else:
        answer2 += step

#------------Answer 2----------------#
#found = 0
#for x in range(guide, guide - ceil(base/2), -1):
    #print(x,answer)
#    if x == n:
#        print("Method 2",answer)
#        found = 1
#        break
#    else:
#        answer -= 1
#if found == 0:
#    answer += 2

#    guide = guide - ceil(base/2)
#    for x in range(guide, guide - ceil(base/2), -1):
        #print(x,answer)
#        if x == n:
#            print("Method 2",answer)
#            break
#        else:
#            answer += 1

