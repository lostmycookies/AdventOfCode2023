# Advent of Code 2023 - Day 1, Part 1
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 14:59:06 2023 
"""

with open('input.txt') as f:
    lines = f.read().splitlines()  
    #text = f.read()

text = open("input.txt").read()

str2num = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e",
}

result = 0

def sum_digits(inputlist):
    result = 0
    for line in inputlist:
        temp = []
        for character in line:
            if character.isdigit():
                temp.append(character)
                #print(temp)
        result += int(temp[0] + temp[-1])
    return result

def replace_words(inputtext):
    for key, value in str2num.items():
        inputtext = inputtext.replace(key, value)
        #print(inputtext)
    return inputtext.splitlines()

### Answer Day 1 ###

print("\n\n The sum of all digits for part 1 is %s." % str(sum_digits(lines)))

### Answer Day 2 ###

print("\n\n The sum of all digits for part 2 is %s." % str(sum_digits(replace_words(text))))


        



