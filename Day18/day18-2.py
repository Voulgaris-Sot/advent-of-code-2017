import sys
from collections import defaultdict, deque

instructions = []
with open(sys.argv[1],'r') as f:
    instructions = [line.split() for line in f]

#global variables
length = len(instructions)
sendA = deque()
sendB = deque()
terminatedA = False
terminatedB = False
waitA = False
waitB = False
answer = 0

def get(registers, X):
    try:
        val = int(X)
    except ValueError:
        val = registers[X]
    return val


def run(i, pid, registers):
    global sendA, sendB, terminatedA, terminatedB, answer
    global waitA, waitB

    has_sent = False
    while(i>=0 and i<length):
        command = instructions[i]

        if command[0] == "snd":
            has_sent = True
            val = get(registers, command[1])
            if pid == 0:
                sendA.appendleft(val)
            else:
                sendB.appendleft(val)
                answer += 1

        if command[0] == "rcv":
            if pid == 0:
                if sendB:
                    registers[command[1]] = sendB.pop()
                    waitA = False
                else:
                    waitA = True
                    if waitB and not has_sent:
                        print("Deadlock")
                        terminatedA = True
                        terminatedB = True
                    return i,registers
            if pid == 1:
                if sendA:
                    registers[command[1]] = sendA.pop()
                    waitB = False
                else:
                    waitB = True
                    if waitA and not has_sent:
                        print("Deadlock")
                        terminatedA = True
                        terminatedB = True
                    return i,registers

        if len(command) > 2:
            val = get(registers, command[2])
        if command[0] == "set":
            registers[command[1]] = val
        if command[0] == "add":
            registers[command[1]] += val
        if command[0] == "mul":
            registers[command[1]] *= val
        if command[0] == "mod":
            registers[command[1]] %= val
        if command[0] == "jgz":
            val2 = get(registers, command[1])
            if val2 > 0:
                i += val - 1
        i += 1
    if pid == 0:
        print("A was terminated")
        terminatedA = True
        waitA = True #so we dont have to check in deadlock for termination
    else:
        print("B was terminated")
        terminatedB = True
        waitB = True
    return i, registers

registersA = defaultdict(int)
registersB = defaultdict(int)
registersB['p'] = 1
iA = iB = 0
while (not terminatedA) or (not terminatedB):
    if not terminatedA:
        iA, registersA = run(iA, 0, registersA)
    if not terminatedB:
        iB, registersB = run(iB, 1, registersB)

print(answer)
