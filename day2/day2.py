# Advent of code 2019
# Day 1 by Gabriel Périard-Tremblay
import sys

def operation(op, a, b):
    if op == 1:
        return a + b
    elif op == 2:
        return a * b
    else:
        return 'FUCK'

def part1():
    with open("input.txt", "r") as file:
        for line in file.readlines():
            values = line.split(',')
            for i in range(len(values)):
                values[i] = int(values[i])
            values[1] = 12
            values[2] = 2
            op_pos = 0
            while True:
                if values[op_pos] == 99:
                    print(f"Part 1 answer: {values[0]}")
                    break
                values[values[op_pos + 3]] = operation(values[op_pos], values[values[op_pos + 1]], values[values[op_pos + 2]])
                op_pos += 4



def part2():
    for j in range(0,100):
        for k in range(0,100):
            noun = j
            verb = k
            values = '1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,9,1,19,1,19,6,23,2,6,23,27,2,27,9,31,1,5,31,35,1,35,10,39,2,39,9,43,1,5,43,47,2,47,10,51,1,51,6,55,1,5,55,59,2,6,59,63,2,63,6,67,1,5,67,71,1,71,9,75,2,75,10,79,1,79,5,83,1,10,83,87,1,5,87,91,2,13,91,95,1,95,10,99,2,99,13,103,1,103,5,107,1,107,13,111,2,111,9,115,1,6,115,119,2,119,6,123,1,123,6,127,1,127,9,131,1,6,131,135,1,135,2,139,1,139,10,0,99,2,0,14,0'.split(',')
            for i in range(len(values)):
                values[i] = int(values[i])
            values[1] = j
            values[2] = k
            op_pos = 0
            while True:
                if values[op_pos] == 99:
                    result = values[0]
                    if result == 19690720:
                        print(f"Part 2 answer: {noun}-{verb}")
                    break
                output = operation(values[op_pos], values[values[op_pos + 1]], values[values[op_pos + 2]])
                if output == 'FUCK':
                    break
                values[values[op_pos + 3]] = output
                op_pos += 4

if __name__ == "__main__":
    part1()
    part2()
