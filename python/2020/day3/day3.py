from functools import reduce
import numpy as np
import pandas as pd

file = 'day3/input.txt'


gradient_list = [(1,1),(3,1),(5,1),(7,1),(1,2)] # structure is (right,down)

if __name__ == "__main__":
    with open(file, 'r') as reader:
        line = reader.readline().strip('\n')

        n = len(line)
        i = 0
        trees_dict = {k:0 for k in gradient_list }
        position_dict = {k:0 for k in gradient_list}

        while line != '':

            for k,v in trees_dict.items():
                if i%(k[1])==0:
                    if line[position_dict[k]]=='#':
                        trees_dict[k]+=1
                    position_dict[k] = (position_dict[k]+k[0]) % n

            line = reader.readline().strip('\n')
            i+=1

        print(trees_dict)
        print("First Part")
        print(trees_dict[(3,1)])
        print("Second Part")
        s=reduce(lambda a,b: a*b,trees_dict.values())
        print(int(s))
        print(trees_dict)