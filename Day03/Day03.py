# Advent of Code 2023 - Day 3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 14:59:06 2023
"""

import re
from operator import mul # multiplies exactly two numbers

# read input file

with open('input.txt') as f:
    lines = f.read().splitlines()  

# variable initialization

chars = "0123456789"
j = 0
sum = 0

# function definitions

def add_dots (lines):
    matrix_len = len(lines[0])+2
    dot_line = ["." * matrix_len]
    dot_matrix = []
    dot_body = ["." + line + "." for line in lines]
    dot_matrix = dot_line + dot_body + dot_line
    return dot_matrix

def symbol_check (lines,number, i, j):
    #print(number,len(number),i,j)
    start = i - int(len(number))
    #print("Start", start)
    stop = i
    #print("Stop", stop)
    for k in range(start-1, stop+1):
        for l in range(j-2, j+1):
            #print (lines[l][k],l,k)
            if lines[l][k] not in "0123456789.":
                #print("Symbol found at", l, k, lines[l][k])
                return int(number)
    else:
        return 0
    
# add dots around the initial matrix

lines = add_dots(lines)

# iterate through the matrix and check for numbers next to symbols

for line in lines:
    #print(line)
    number = ""
    i = 0
    j += 1
    last_char = int(len(line))
    for char in line:
        if char in chars:
            number += char
        if char not in chars and number != "":
            #print (number)
            sum += symbol_check(lines,number, i, j)
            number = ""
        i += 1

def part2(lines):
    gear_regex = r'\*'
    gears = dict()
    for i, line in enumerate(lines):
        for m in re.finditer(gear_regex, line):
            gears[(i, m.start())] = []

    number_regex = r'\d+'
    for i, line in enumerate(lines):
        for m in re.finditer(number_regex, line):
            for r in range(i-1, i+2):
                for c in range(m.start()-1, m.end()+1):
                    if (r, c) in gears:
                        gears[(r, c)].append(int(m.group()))

    gear_ratio_sum = 0
    for nums in gears.values():
        if len(nums) == 2:
            gear_ratio_sum += mul(*nums)

    return gear_ratio_sum

print("Part 1:", sum)
print('Part 2:', part2(lines))

