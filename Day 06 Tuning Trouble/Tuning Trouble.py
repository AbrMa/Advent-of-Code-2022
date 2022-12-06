file_name = "input.txt"

with open(file_name, "r") as file:
    for line in file:
        line = line.replace("\n", "")
        #Part 1
        for i in range(len(line)):
            unique = set(list(line[i:i+4]))
            if len(unique) == 4:
                print(i+4)
                break
        #Part 2
        for i in range(len(line)):
            unique = set(list(line[i:i+14]))
            if len(unique) == 14:
                print(i+14)
                break 