import pandas as pd
import numpy as np
import copy

file = "day17/input.txt"


def neighbours(coord: tuple, dim:int) -> list:
    lst = []

    if dim == 3:
        for i in range(-1,2):
            for j in range(-1,2):
                for k in range(-1,2):
                    if i!= 0 or j!= 0 or k!=0:
                        lst.append((coord[0] + i, coord[1] + j , coord[2] + k))

    elif dim == 4:

        for i in range(-1, 2):
            for j in range(-1, 2):
                for k in range(-1, 2):
                    for l in range(-1,2):
                        if i != 0 or j != 0 or k != 0 or l !=0:
                            lst.append((coord[0] + i, coord[1] + j, coord[2] + k, coord[3] + l))
        xxx = 1
    return lst

def active_neighbours(coord: tuple, map_: dict, dim :int) -> int:
    adjacent_cells = neighbours(coord, dim)

    active = 0

    for neighbour in adjacent_cells:
        if map_.get(neighbour):
            active += 1

    return active

def evolve_map(map_:dict,dim:int = 3) -> dict:
    
    lst = set()
    new_map = {}

    for val in map_.keys():

        lst.add(val)
        lst |= set(neighbours(val,dim))

    for val in lst:
        active_neighbours_count = active_neighbours(val,map_,dim)
        if map_.get(val):
            if active_neighbours_count == 2:
                new_map[val] = 1

        if active_neighbours_count == 3:
            new_map[val] =1 


    return new_map

if __name__ == "__main__":
    with open(file, 'r') as reader:
        line = reader.readline().strip()
        x = 0
        z = 0
        w = 0
        map_a = {}
        map_b = {}
        while line != "":
            for i in range(len(line)):
                if line[i] == '#':
                    map_a[(x,i,z)] =  1
                    map_b[(x,i,z,w)] = 1
            x += 1
            line = reader.readline().strip()


    active_cubes = 0
    active_cubes_b = 0

    for i in range(6):
        map_a = evolve_map(map_a)
        map_b = evolve_map(map_b,4)
        active_cubes = len(map_a.keys())
        active_cubes_b = len(map_b.keys())
        xxx = 1

    print("Answer to Part A")
    print(active_cubes)
    print("Answer to Part B")
    print(active_cubes_b)
    print("Le Fin")
