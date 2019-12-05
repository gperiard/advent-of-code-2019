import pprint
from copy import copy


def get_manhattan_distance(a: tuple, b: tuple):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def get_input():
    wires = []
    with open("input.txt", "r") as file:
        for line in file.readlines():
            wires.append(line.split(","))

    return wires


def directions_to_coordinates(directions: list) -> list:
    coordinates = {}
    current_position = [0, 0]
    total_distance = 0
    for direction in directions:
        sens = direction[:1]
        distance = int(direction[1:])

        for i in range(distance):
            total_distance += 1
            if sens == "U":
                current_position[1] += 1
            elif sens == "D":
                current_position[1] -= 1
            elif sens == "R":
                current_position[0] += 1
            elif sens == "L":
                current_position[0] -= 1
            else:
                print("error")

            coordinates[f"{current_position[0]}_{current_position[1]}"] = total_distance

    return coordinates


def part1():
    wires = get_input()
    # wires = [
    #     ["R75", "D30", "R83", "U83", "L12", "D49", "R71", "U7", "L72"],
    #     ["U62", "R66", "U55", "R34", "D71", "R55", "D58", "R83"],
    # ]
    # wires = [
    #     "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51".split(","),
    #     "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7".split(","),
    # ]

    print("input")

    coordinates = []
    for wire in wires:
        coordinates.append(directions_to_coordinates(wire))

    print("coordinates")

    intersections = set(coordinates[0].keys()) & set(coordinates[1].keys())

    distances = []
    timeto = {}
    for i in intersections:
        distances.append(get_manhattan_distance([0, 0], [int(a) for a in i.split("_")]))
        timeto[f"{i}"] = coordinates[0][i] + coordinates[1][i]

    print(f"Answer part 1 is {min(distances)}")
    print(f"Answer part 2 is {timeto[min(timeto, key=timeto.get)]}")


if __name__ == "__main__":
    part1()
