#!/usr/bin/python3

input = open("day4a.input.txt", "r")
# input = open("day4.sample.txt", "r")

def split_to_tuple(line):
    """Split read line into tuple list of ints"""
    worker_left = line.rstrip('\n').split(',')[0].split('-')
    worker_left = [int(j) for j in worker_left]
    worker_right = line.rstrip('\n').split(',')[1].split('-')
    worker_right = [int(k) for k in worker_right]
    return worker_left, worker_right

total_same_work = 0
total_overlap = 0
for i in input:
    i = split_to_tuple(i)
    left_range = set(range(i[0][0],i[0][1] + 1))
    right_range = set(range(i[1][0],i[1][1] + 1))

    if set(left_range).issubset(right_range) or set(right_range).issubset(left_range):
        total_same_work += 1
    if set(left_range) & set(right_range):
        total_overlap +=1

print("1st question answer: \t",total_same_work)
print("2nd question answer: \t",total_overlap)