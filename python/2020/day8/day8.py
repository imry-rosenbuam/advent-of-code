import pandas as pd
import numpy as np

file = "day8/input.txt"

batch_file = list()

processed_dict = {}
processsing_complete = 0
part_b_acc = 0


def batch_processing(i: int, main_route: int = 1) -> float:
    global processsing_complete
    global part_b_acc

    if processed_dict.get(i):
        print('A loop has been found')
        return 0
    else:
        processed_dict[i] = 1

    if i >= len(batch_file):
        processsing_complete = 1
        print("File has completed processing")
        return 0 

    order, jump = batch_file[i].split(" ")
    if order == "nop":
        acc_a = batch_processing(i+1, main_route)

        if main_route and (processsing_complete < 1):
            acc_b = batch_processing(i+int(jump), 0)
            if processsing_complete:
                part_b_acc = acc_b-acc_a

        processed_dict.pop(i, None)
        return acc_a
    elif order == "jmp":
        acc_a = batch_processing(i+int(jump), main_route)

        if main_route and (processsing_complete < 1):
            acc_b = batch_processing(i+1, 0)
            if processsing_complete:
                part_b_acc = acc_b - acc_a

        processed_dict.pop(i)
        return acc_a
    elif order == "acc":
        acc_a = batch_processing(i+1, main_route)+int(jump)

        processed_dict.pop(i, None)
        return acc_a
    else:
        acc_a = 0
        return acc_a


if __name__ == "__main__":
    with open(file, 'r') as reader:
        line = reader.readline()
        while line != "":
            batch_file.append(line.strip())
            line = reader.readline()

    part_a = batch_processing(0)
    print("Answer for Part A:")
    print(part_a)
    print("Answer for Part B:")
    print(part_a+part_b_acc)
    print("Le Fin")
