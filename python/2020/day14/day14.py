import numpy as np
from numpy.core.numeric import indices
import pandas as pd
import re

file = "day14/input.txt"

pattern_mask = "mask = (\w+)"
pattern_assign = "mem\[(\d+)\] = (\d+)"


def cell_insert(number: int, mask_: str) -> int:
    
    num_bin = format(number,'036b')
    new_num = []
    for i in range(len(num_bin)):
        if mask_[i] == 'X':
            new_num.append(num_bin[i])
        else:
            new_num.append(mask_[i])
    new_num = "".join(new_num)
    new_num = int(new_num,2)
    return new_num

def cell_insert_v2(cell_:int, mask_:str) -> list:
    
    cell_bin = format(cell_, '036b')

    new_cell = list()
    indices = []
    for i in range(len(cell_bin)):
        if mask_[i] == "X" or mask_[i] == "1":
            new_cell.append(mask_[i])
            if mask_[i] == "X":
                indices.append(i)
        else:
            new_cell.append(cell_bin[i])
    new_cells = [new_cell]

    for index in indices:
        for _ in range(len(new_cells)):
            cell_0 = new_cells.pop(0)
            cell_1 = cell_0.copy()
            cell_0[index] = "0"
            cell_1[index] = "1"
            new_cells += [cell_0, cell_1]

    return new_cells

if __name__ == "__main__":
    mask = 'X' * 36 #format(0,'036b')
    mem = {}
    mem_b = {}
    with open(file, 'r') as reader:
        line = reader.readline()
        while line!= "":
            if (match := re.match(pattern_mask, line.strip())):
                mask = match.groups()[0]
            elif (match := re.match(pattern_assign, line.strip())):
                cell,num = match.groups()
                mem[int(cell)] = cell_insert(int(num),mask)
                cells = cell_insert_v2(int(cell), mask)
                for subcell in cells:
                    mem_b[int("".join(subcell),2)] =  int(num)
            line = reader.readline()

    print("Answer to part A:")
    print(sum(mem.values()))
    print("Answer to part B")
    print(sum(mem_b.values()))
    print("Le Fin")
