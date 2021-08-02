import numpy as np
import pandas as pd
import os as os

file = 'day1/input.txt'

report= {}

if __name__=="__main__":
    #part 1
    with open(file, 'r') as reader:
        line = reader.readline()
        while line != '':
            if report.get(2020-int(line)):
                print("Part1")
                print(int(line)*(2020-int(line)))
            report[int(line)] = report.get(int(line),0) + 1
            line = reader.readline()

    keys = list(map(int,report.keys()))

    # in a similar fashion to what we did before we can create a dictionary 
    # of the dual values and take the complexity from o(n^3) to o(n^2) but sacrfice o(n^2) of memeory
    for i in range(len(keys)):
        for j in range(i,len(keys)):
           for k in range(j,len(keys)):
               if (i !=j) and (k != j):
                   if (int(keys[i])+int(keys[j])+int(keys[k]))==2020:
                       print("Part 2")
                       print(keys[i]*keys[j]*keys[k])

    print("Le Fin")