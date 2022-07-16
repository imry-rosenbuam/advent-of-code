import numpy as np
import pandas as pd
import os

print(os.getcwd())

with open("day1/input.txt") as file:
    
    lines = file.readlines()
    #lines = [199,200,208,210,200,207,240,269,260,263]
    #lines = [1,1,1,1]
    lines = np.array(list(map(lambda x: int(x),lines)))
    
    lines_shift = np.roll(lines,1)
    diff = lines - lines_shift
    ex1 = diff[1:] > 0
    print("solution to part A:")
    print(sum(ex1))
    window_size = 3
    print("part B answer is:")
    cs = lines.cumsum()
    cs[window_size:] = cs[window_size:] - cs[:-1 *window_size]
    window = cs[window_size - 1:]
    print(window)
    window_diff = window - np.roll(window,1)
    print(sum(window_diff[1:] > 0))