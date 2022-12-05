#!/usr/bin/python3

import string

input = open("./day3a.input.txt", "r")

def common(set1, set2, set3 = ''):
    if set3 == '':
        try:
            return set.intersection(set(set1), set(set2)).pop()
        except:
            return None
    else:
        try:
            return set.intersection(set(set1), set(set2), set(set3)).pop()
        except:
            return None

alphas = list(string.ascii_letters)
nums = list(range(1,53))
alpha_map = dict(zip(alphas, nums))

total = 0
for line in input:
    half = int(len(line)/2)
    first_half = line[:half]
    second_half = line[half:]

    common_char = common(first_half, second_half)
    total += int(alpha_map[common_char])

input2 = open("./day3a.input.txt", "r")
count = 0
group_lines = []
total2 = 0
for line in input2:
    line = line.rstrip('\n')
    group_lines.append(line)
    if count < 2:
        count += 1
    else:
        result = common(group_lines[0], group_lines[1], group_lines[2])
        total2 += int(alpha_map[result])
        count = 0
        group_lines = []

print("1st question answer: \t", total)
print("2nd question answer: \t", total2)