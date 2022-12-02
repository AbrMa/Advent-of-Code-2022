with open('input.txt', 'r') as f:
    elves = []
    calories = 0

    for line in f:
        if line != "\n":
            calories += int(line)
        else:
            elves.append(calories)
            calories = 0

    elves.append(calories)
    calories = 0

    #Part 1
    elves.sort()
    print(elves[-1])

    #Part 2
    top_three = elves[-1] + elves[-2] + elves[-3]
    print(top_three)
