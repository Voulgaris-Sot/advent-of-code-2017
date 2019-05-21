import sys

all_registers = {}
my_max = 0

with open(sys.argv[1],'r') as f:
    for line in f:
        instruction = line.split()
        #print("before")
        #print(all_registers)

        register = instruction[0]
        operation = instruction[1]
        amount = int(instruction[2])
        cond_register = instruction[4]
        condition = instruction[5]
        cond_amount = int(instruction[6])

        if register not in all_registers:
            all_registers[register] = 0
        if cond_register not in all_registers:
            all_registers[cond_register] = 0

        if condition == ">":
            if all_registers[cond_register] > cond_amount:
                if operation == "inc":
                    all_registers[register] += amount
                else:
                    all_registers[register] -= amount

        if condition == "<":
            if all_registers[cond_register] < cond_amount:
                if operation == "inc":
                    all_registers[register] += amount
                else:
                    all_registers[register] -= amount

        if condition == ">=":
            if all_registers[cond_register] >= cond_amount:
                if operation == "inc":
                    all_registers[register] += amount
                else:
                    all_registers[register] -= amount

        if condition == "<=":
            if all_registers[cond_register] <= cond_amount:
                if operation == "inc":
                    all_registers[register] += amount
                else:
                    all_registers[register] -= amount

        if condition == "==":
            if all_registers[cond_register] == cond_amount:
                if operation == "inc":
                    all_registers[register] += amount
                else:
                    all_registers[register] -= amount


        if condition == "!=":
            if all_registers[cond_register] != cond_amount:
                if operation == "inc":
                    all_registers[register] += amount
                else:
                    all_registers[register] -= amount
        #print("after")
        #print(all_registers)
        my_max = max(max(all_registers.values()), my_max)

#Part1
print(max(all_registers.values()))
#Part2
print(my_max)

