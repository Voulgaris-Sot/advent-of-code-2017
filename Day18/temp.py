import sys
from collections import defaultdict

instructions = []
with open(sys.argv[1],'r') as f:
    for line in f:
        ins = line.split()
        #malaka ti xazo einai auto poy exo kanei edo??
        if ins[0] == "snd" or ins[0] == "rcv":
            instructions.append([ins[0], ins[1]])
        else:
            instructions.append([ins[0], ins[1], ins[2]])

length = len(instructions)
sendA = []
sendB = []
terminatedA = False
terminatedB = False
answer = 0

waitA = False
waitB = False


def run(i, pid, registers):
    global sendA, sendB, terminatedA, terminatedB, answer
    global waitA, waitB

    has_sent = False
    actually_run = False
    while(i>=0 and i<length):
        command = instructions[i]
        if command[0] == "snd":
            has_sent = True
            try:
                val = int(command[1])
            except ValueError:
                val = registers[command[1]]
            if pid == 0:
                sendA.insert(0, val)
     #           print(sendA)
            else:
                sendB.insert(0, val)
                answer += 1
    #            print(sendB)

        if command[0] == "rcv":
            if pid == 0:
                if sendB:
                    registers[command[1]] = sendB.pop()
                 #   print(sendB)
                else:
                    waitA = True
                    if waitB and not has_sent:
                        terminatedA = True
                    return i,registers, actually_run
            if pid == 1:
                if sendA:
                    registers[command[1]] = sendA.pop()
    #                print(sendA)
                else:
                    waitB = True
                    if waitA and not has_sent:
                        terminatedB = True
                    return i,registers, actually_run


        if len(command) > 2:
            try:
                val = int(command[2])
            except ValueError:
                val = registers[command[2]]
        if command[0] == "set":
            registers[command[1]] = val
        if command[0] == "add":
            registers[command[1]] += val
        if command[0] == "mul":
            registers[command[1]] *= val
        if command[0] == "mod":
            registers[command[1]] %= val
        if command[0] == "jgz":
            if registers[command[1]] > 0:
                i += val
                actually_run = True
                continue
        actually_run = True
        i += 1
    if pid == 0:
        print("A was terminated")
        terminatedA = True
    else:
        print("B was terminated")
        terminatedB = True
    return i, registers, actually_run#false to signify that it wont run again

registersA = defaultdict(int)
registersB = defaultdict(int)
registersB['p'] = 1
iA = 0
iB = 0
ii = 0
while (not terminatedA) or (not terminatedB):
    if not terminatedA:
        iA, registersA, runA = run(iA, 0, registersA)
    if not terminatedB:
        iB, registersB, runB = run(iB, 1, registersB)
    if (not runA) and (not runB):
        print("Deadlock")
        terminatedA = True
        terminatedB = True
    if ii%100:
        print(runA, runB, len(sendA),len(sendB))
    ii += 1

#print(registersA)
#print(registersB)
print(answer)
