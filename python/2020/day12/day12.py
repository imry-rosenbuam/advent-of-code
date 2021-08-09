from typing import NamedTuple
import pandas as pd
import numpy as np
import re
import math
from collections import namedtuple

pattern = "([a-zA-Z])(\d+)"
file = "day12/input.txt"


def change_position_b(position_: dict, direction: str, magnitude: int) -> None:

    if direction == 'N':
        position_['waypoint']['y'] += magnitude
    elif direction == 'S':
        position_['waypoint']['y'] -= magnitude
    elif direction == 'E':
        position_['waypoint']['x'] += magnitude
    elif direction == 'W':
        position_['waypoint']['x'] -= magnitude
    elif direction == 'F':
        position_['x'] += magnitude * position_['waypoint']['x']
        position_['y'] += magnitude * position_['waypoint']['y']
    elif direction == 'L':
        norm = math.sqrt(position_['waypoint']['x'] **
                         2 + position_['waypoint']['y'] ** 2)
        degree = math.atan2(
            position_['waypoint']['y'], position_['waypoint']['x']) + math.radians(magnitude)
        position_['waypoint']['x'] = norm * math.cos(degree)
        position_['waypoint']['y'] = norm * math.sin(degree)
    elif direction == 'R':
        norm = math.sqrt(position_['waypoint']['x'] **
                         2 + position_['waypoint']['y'] ** 2)
        degree = math.atan2(
            position_['waypoint']['y'], position_['waypoint']['x']) - math.radians(magnitude)
        position_['waypoint']['x'] = norm * math.cos(degree)
        position_['waypoint']['y'] = norm * math.sin(degree)

    return None


def change_position(position_: dict, direction: str, magnitude: int) -> None:

    if direction == 'N':
        position_['y'] += magnitude
    elif direction == 'S':
        position_['y'] -= magnitude
    elif direction == 'E':
        position_['x'] += magnitude
    elif direction == 'W':
        position_['x'] -= magnitude
    elif direction == 'F':
        position_['x'] += magnitude * int(math.cos(position_['facing']))
        position_['y'] += magnitude * int(math.sin(position_['facing']))
    elif direction == 'L':
        position_['facing'] += math.radians(magnitude)
    elif direction == 'R':
        position_['facing'] -= math.radians(magnitude)

    return None


if __name__ == "__main__":
    with open(file, 'r') as reader:
        line = reader.readline()
        # position is x-axis,y-axis and which is which direction we are facing in radians
        position = {'x': 0, 'y': 0, 'facing': 0}
        position_b = {'x': 0, 'y': 0, 'waypoint': {'x': 10, 'y': 1}}

        while line != "":
            s = re.match(pattern, line.strip())
            direction, magnitude = s.groups()
            magnitude = int(magnitude)
            change_position(position, direction, magnitude)
            change_position_b(position_b, direction, magnitude)
            #print("x:{0},y:{1},facing:{2}".format(position['x'],position['y'],math.degrees(position['facing'])))
            print("x:{0},y:{1},waypoint:({2},{3})".format(
                position_b['x'], position_b['y'], position_b['waypoint']['x'], position_b['waypoint']['y']))
            line = reader.readline()
    print("Answer to Part A:")
    print(int(abs(position['x']) + abs(position['y'])))
    print("Answer to Part B")
    print((abs(position_b['x']) + abs(position_b['y'])))
    print("Le Fin")
