interval_pairs = []

with open("./input.txt", "r") as f:
    for line in f:
        line = line.replace("\n", "")
        first_section, second_section = line.split(',')
        f_beg, f_end = [int(num) for num in first_section.split('-')]
        s_beg, s_end = [int(num) for num in second_section.split('-')]
        interval_pairs.append((f_beg, f_end, s_beg, s_end))

#First Part
fully_contains = 0
for f_beg, f_end, s_beg, s_end in interval_pairs:
    if (f_beg <= s_beg <= s_end <= f_end or
        s_beg <= f_beg <= f_end <= s_end):
        fully_contains += 1
print(fully_contains)

#Second Part
overlaps = 0
for f_beg, f_end, s_beg, s_end in interval_pairs:
    if (f_beg <= s_beg <= f_end or
        f_beg <= s_end <= f_end or
        s_beg <= f_beg <= s_end or
        s_beg <= f_end <= s_end ):
        overlaps += 1
print(overlaps)