# Advent of code 2019
# Day 1 by Gabriel Périard-Tremblay

def part1():
    total = 0
    with open("input.txt", "r") as file:
        for line in file.readlines():
            mass = int(line)
            total += int((mass/3)) - 2

        print(f"Part 1 answer: {total}")

def fuel_needed(mass, fuel=0):
    total_fuel = fuel
    fuel = int(mass/3) - 2

    if fuel <= 0:
        return total_fuel

    total_fuel += fuel
    return fuel_needed(fuel, total_fuel)

def part2():
    total = 0
    with open("input.txt", "r") as file:
        for line in file.readlines():
            total += fuel_needed(int(line))

        print(f"Part 2 answer: {total}")

if __name__ == "__main__":
    part1()
    part2()
