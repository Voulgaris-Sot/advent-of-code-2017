import sys
from collections import defaultdict, deque

instructions = []
with open(sys.argv[1],'r') as f:
    instructions = [line.split() for line in f]

def get(registers, X):
    try:
        val = int(X)
    except ValueError:
        val = registers[X]
    return val

def run(i, registers):

    length = len(instructions)
    answer = -1
    while(i>=0 and i<length):
        command = instructions[i]

        if command[0] == "snd":
            val = get(registers, command[1])
            answer = val

        if command[0] == "rcv":
            if registers[command[1]] != 0:
                break

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
    return answer

registers = defaultdict(int)
print(run(0, registers))
