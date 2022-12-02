#!/usr/bin/python3

input = open("day2a.input.txt", "r")

def clean_num(num):
    try:
        return int(num)
    except ValueError:
        return None
score = 0
for line in input:
    clean_line = []
    if line[0] == "A":
        clean_line.append(1)
    if line[0] == "B":
        clean_line.append(2)
    if line[0] == "C":
        clean_line.append(3)

    if line[-2] == "X":
        clean_line.append(1)
    if line[-2] == "Y":
        clean_line.append(2)
    if line[-2] == "Z":
        clean_line.append(3)

    sum = int(0) 
    # DRAW
    if clean_line[0] == clean_line[-1]:
        sum += int(3)
        if clean_line[-1] == 1:
            sum += int(1)
        if clean_line[-1] == 2:
            sum += int(2)
        if clean_line[-1] == 3:
            sum += int(3)
    # LOSS
    if clean_line[0] == 2 and clean_line[-1] == 1: # Paper, Rock // LOSS 1 + 0
        sum += int(1)
    if clean_line[0] == 3 and clean_line[-1] == 2: # Scissors, Paper // LOSS 2 + 0
        sum += int(2)
    if clean_line[0] == 1 and clean_line[-1] == 3: # Rock, Scissors // LOSS 3 + 0
        sum += int(3)
    # WIN
    if clean_line[0] == 3 and clean_line[-1] == 1: # Scissors, Rock // WIN 1 + 6
        sum += int(1) + int(6)
    if clean_line[0] == 1 and clean_line[-1] == 2: # Rock, Paper // WIN 2 + 6
        sum += int(2) + int(6)
    if clean_line[0] == 2 and clean_line[-1] == 3: # Paper, Scissors // WIN 3 + 6
        sum += int(3) + int(6)
    score += int(sum)
print("Score from question1: ",score)

score2 = 0
sum2 = 0
input2 = open("day2a.input.txt", "r")
for line in input2:
    clean_line = []
    if line[0] == "A":
        clean_line.append(1)
    if line[0] == "B":
        clean_line.append(2)
    if line[0] == "C":
        clean_line.append(3)

    if line[-2] == "X":
        clean_line.append(1)
    if line[-2] == "Y":
        clean_line.append(2)
    if line[-2] == "Z":
        clean_line.append(3)

    if clean_line[-1] == 1:
        # Loss
        if clean_line[0] == 1:
            sum2 += clean_num(3)
        if clean_line[0] == 2:
            sum2 += clean_num(1)
        if clean_line[0] == 3:
            sum2 += clean_num(2)
    if clean_line[-1] == 2:
        sum2 += clean_num(3) # Draw
        if clean_line[0] == 1:
            sum2 += clean_num(1)
        if clean_line[0] == 2:
            sum2 += clean_num(2)
        if clean_line[0] == 3:
            sum2 += clean_num(3)
    if clean_line[-1] == 3:
        sum2 += clean_num(6) # Win
        if clean_line[0] == 1:
            sum2 += clean_num(2)
        if clean_line[0] == 2:
            sum2 += clean_num(3)
        if clean_line[0] == 3:
            sum2 += clean_num(1)

score2 = sum2
print("Score from question2: ", score2)