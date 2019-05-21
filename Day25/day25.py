import sys
from collections import deque

state = 'A'
tape = deque([0])
cursor = 0

def move_right():
    global cursor,tape
    if cursor == len(tape)-1:
        tape.append(0)
    cursor += 1

def move_left():
    global cursor,tape
    if cursor == 0:
        tape.appendleft(0)
    else:
        cursor -= 1

for i in range(12964419):
    if state == 'A':
        if tape[cursor] == 0:
            tape[cursor] = 1
            move_right()
            state = 'B'
        else:
            tape[cursor] = 0
            move_right()
            state = 'F'
    elif state == 'B':
        if tape[cursor] == 0:
            #tape[cursor] = 0
            move_left()
            state = 'B'
        else:
           #tape[cursor] = 1
            move_left()
            state = 'C'
    elif state == 'C':
        if tape[cursor] == 0:
            tape[cursor] = 1
            move_left()
            state = 'D'
        else:
            tape[cursor] = 0
            move_right()
            state = 'C'
    elif state == 'D':
        if tape[cursor] == 0:
            tape[cursor] = 1
            move_left()
            state = 'E'
        else:
            #tape[cursor] = 1
            move_right()
            state = 'A'
    elif state == 'E':
        if tape[cursor] == 0:
            tape[cursor] = 1
            move_left()
            state = 'F'
        else:
            tape[cursor] = 0
            move_left()
            state = 'D'
    elif state == 'F':
        if tape[cursor] == 0:
            tape[cursor] = 1
            move_right()
            state = 'A'
        else:
            tape[cursor] = 0
            move_left()
            state = 'E'
    else:
        print("Unkown State.Exiting.")
        sys.exit()
print(sum(tape),len(tape))
