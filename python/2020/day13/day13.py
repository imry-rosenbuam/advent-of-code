import numpy as np
import pandas as pd
import scipy
from pulp import LpProblem, LpStatus, lpSum, LpVariable, LpMinimize

file = "day13/input.txt"


def bus_contest(busses: list) -> np.int64:

    model = LpProblem(name="buss-contest", sense=LpMinimize)
    t = LpVariable(name="t", lowBound=0, cat="Integer")
    x = {}

    model += t * 1

    for i in range(len(busses)):
        if busses[i] != 0:
            x[i] = LpVariable(name=f"x{i}", lowBound=1, cat="Integer")
            model += (t - x[i] * busses[i] == i)

    status = model.solve()

    print(f"objective: {model.objective.value()}")

    for var in model.variables():
        print(f"{var.name}: {var.value()}")

    print(f"status: {model.status}, {LpStatus[model.status]}")

def contest(busses:list) -> np.int64:
    vals = []
    vals2 = []
    for i in range(len(busses)):
        if busses[i]!= 0:
            vals.append(((busses[i]-i) % busses[i],busses[i]))
            vals2.append((i,busses[i]))

    #vals = [(4,5),(3,4),(0,3)]

    params = sorted(vals,key=lambda x:x[1])
    params_2 = params.copy()
    
    x,n = params.pop()

    while len(params):
        x1,n1 = params.pop(0)

        while (x % n1) != x1:
            x += n

        n *= n1
    
    #x2 = 1068781
    mods = [(x+y[0]) % y[1] for y in vals2]
    #mods2 = [(x2+y[0]) % y[1] for y in vals2]
    sol = x
    print(sol)


if __name__ == "__main__":

    with open(file, 'r') as reader:
        line = reader.readline()
        earliest_timestamp = int(line)
        line = reader.readline().strip().split(',')
        buses = [int(x) for x in line if x != 'x']
        buses_b = [(lambda x: int(x) if x != 'x' else 0)(x) for x in line]
    times = [((x - (earliest_timestamp % x) if x %
              earliest_timestamp != 0 else 0), x)for x in buses]
    print("Answer to Part A:")
    mn = min(times, key=lambda x: x[0])
    print(mn[0] * mn[1])
    print("Answer to Part B")
    contest(buses_b)
    print("Le Fin")
