import re

# read input file
with open('input.txt') as f:
    lines = f.read().splitlines()

def nr_of_wins(line):
    match = re.split(":", line)[1].split("|")
    win_numbers = re.findall("\d+", match[0])
    own_numbers = re.findall("\d+", match[1])
    nr_of_wins = 0
    for win_number in win_numbers:
        if win_number in own_numbers:
            nr_of_wins += 1
    return nr_of_wins

# calculate points based on the number of wins
def point_value (line):
    wins = nr_of_wins(line)
    if wins == 0:
        return 0
    else:
        point_results = 2 ** (wins-1)
    return point_results

total_points = 0

for line in lines:
    total_points += point_value(line)

# print the total points
print("Total points:", total_points)


###### part 2 ######

scratch_total = 0

scratch_list = [1] * len(lines)

for index, line in enumerate(lines):
    n = nr_of_wins(line)
    for i in range(n):
        scratch_list[index + i + 1] += scratch_list[index]

print("Total # of scratch tickets:", sum(scratch_list))