import sys
from collections import defaultdict, deque

instructions = []
with open(sys.argv[1],'r') as f:
    instructions = [line.split() for line in f]

def get(X):
    global registers
    try:
        val = int(X)
    except ValueError:
        val = registers[X]
    return val

def run(i, registers):
    length = len(instructions)
    answer = 0
    while(i>=0 and i<length):
        command = instructions[i]

        val = get(command[2])
        if command[0] == "set":
            registers[command[1]] = val
        if command[0] == "sub":
            registers[command[1]] -= val
        if command[0] == "mul":
            registers[command[1]] *= val
            answer += 1
        if command[0] == "jnz":
            val2 = get(command[1])
            if val2 != 0:
                i += val - 1
        if command[0] == "jmp":
            i += val - 1
        i += 1
    return answer

registers = defaultdict(int)
print(run(0, registers))
