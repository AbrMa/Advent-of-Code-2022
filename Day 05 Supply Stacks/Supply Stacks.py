from collections import defaultdict

file_name = "./input.txt"

original_stacks = defaultdict(list)
moves = []

with open(file_name, "r") as file:
    for line in file:
        if line[0] != "m":
            for idx, char in enumerate(line):
                if char == "[":
                    original_stacks[(idx//4) + 1].append(line[idx+1])
        else:
            quantity = int(line[line.index('e')+1:line.index('f')])
            origin = int(line[line.index("m ")+2:line.index('t')])
            destiny = int(line[line.index("o ")+2:])
            moves.append((quantity, origin, destiny))

for stack_num in range(1, len(original_stacks)+1):
    original_stacks[stack_num] = list(reversed(original_stacks[stack_num]))

#Part 1
stacks = {key: val for key, val in original_stacks.items()}

for quantity, origin, destiny in moves:
    removed = []
    for i in range(quantity):
        removed.append(stacks[origin].pop())
    #Uncomment next line for answer of Part 2 
    #removed.reverse()
    stacks[destiny] += removed

ans = []
for stack_num in range(1, len(stacks)+1):
    ans.append(stacks[stack_num][-1])

print("".join(ans))