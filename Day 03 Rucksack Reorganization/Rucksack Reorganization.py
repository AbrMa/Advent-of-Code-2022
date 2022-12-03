import string

rucksacks = []
lower_priorities = {letter: ord(letter)-ord('a')+1 for letter in string.ascii_lowercase}
upper_priorities = {letter: ord(letter)-ord('A')+27 for letter in string.ascii_uppercase}

with open("./input.txt", "r") as f:
    for line in f:
        line = line.replace("\n", "")
        rucksacks.append(line)

# Part 1
sum = 0
for rucksack in rucksacks:
    first = set(rucksack[:len(rucksack)//2])
    second = set(rucksack[len(rucksack)//2:])
    for item in first:
        if item in second:
            if item.islower():
                sum += lower_priorities[item]
            else:
                sum += upper_priorities[item]

print(sum)

#Part 2
sum, i = 0, 1
group = []
for rucksack in rucksacks:
    group.append(rucksack)
    if i % 3 == 0:
        first, second, third = group
        first, second, third, = set(first), set(second), set(third)
        for item in first:
            if item in second and item in third:
                if item.islower():
                    sum += lower_priorities[item]
                else:
                    sum += upper_priorities[item]
                break
        group.clear()
    i += 1

print(sum)