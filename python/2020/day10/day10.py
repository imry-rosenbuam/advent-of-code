import pandas as pd
import numpy as np
import bisect

file = "day10/input.txt"

adapters = [0]


ways_to_the_end = {} #a dictionary of a node in the adapter graph and how many routes there are to the terminal node

def adapters_combinations(adapter_index:int) -> int:
    if ways_to_the_end.get(adapter_index,None):
        return ways_to_the_end[adapter_index]
    
    paths = 0

    if adapter_index == len(adapters) - 1:
        return 1
    elif adapter_index >= len(adapters):
        return 0

    for i in range(1,4):
        if adapter_index + i < len(adapters):
            if adapters[adapter_index + i] - adapters[adapter_index] <= 3:
                paths += adapters_combinations(adapter_index + i)

    ways_to_the_end[adapter_index] = paths

    return paths

if __name__ == "__main__":
    with open(file,'r') as reader:
        line = reader.readline()
        while line!="":
            bisect.insort(adapters,int(line))            
            line = reader.readline()


    differences = {}
    for i in range(len(adapters)-1):
        diff = adapters[i+1] - adapters[i]
        differences[diff] = differences.get(diff, 0) + 1

    differences[3] = differences.get(3,0) + 1

    print(differences)
    print("Answer to Part A:")
    print(differences.get(1,0) * differences.get(3,0))
    adapters.append(max(adapters) + 3)
    print("Answer to part B:")
    print(adapters_combinations(0))
    print("Le Fin")
