#!/usr/bin/python3

input = open("day1a.input.txt", "r")

def to_num(num):
    try:
        return int(num)
    except ValueError:
        return None

x = 0
a_list = []

for line in input:
    if line.strip() == '':
        a_list.append(x)
        x = 0
    else:
        x = x + to_num(line)

a_list.sort()

print("1st question answer: \t", max(a_list))
print("2nd question answer: \t", sum(a_list[-3:]))