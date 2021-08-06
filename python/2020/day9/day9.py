from typing import OrderedDict
import numpy as np
import pandas as pd
import bisect

file = "day9/input.txt"

preamble = list()
preamble_order = list()
preamble_size = 25
part_a = -1
numbers = list()


def encrypt_weakness(target: int) -> int:
    i = 0
    contigious_set = list()

    s = sum(contigious_set)
    while s != target:
        if s < target:
            contigious_set.append(numbers[i])
            i += 1
        else:
            contigious_set.pop(0)

        # can be improved efficency wise if we remove and add to the sum
        s = sum(contigious_set)

    return min(contigious_set) + max(contigious_set)


if __name__ == "__main__":
    with open(file, 'r') as reader:
        line = reader.readline()
        while line != "":
            num = int(line)
            numbers.append(num)

            if len(preamble) >= preamble_size:
                count = 0
                for x in preamble:
                    diff_pos = bisect.bisect(preamble, num-x)
                    if preamble[diff_pos-1] == (num-x):
                        count += 1

                if count == 0:
                    msg = "NOT valid"
                    if part_a < 0:
                        part_a = num
                else:
                    msg = "valid"
                flag = (sorted(preamble) == sorted(preamble_order))
                print("{0} is {3}, preamble is {1}, ordered is {2}, both set are  equal: {4}".format(
                    num, preamble_order, preamble, msg, flag))
                num_pop = preamble_order.pop(0)
                num_pos = bisect.bisect(preamble, num_pop)-1
                del(preamble[num_pos])

            bisect.insort(preamble, num)
            preamble_order.append(num)
            line = reader.readline()

    print("Answer to Part A:")
    print(part_a)
    print("Answer Part B:")
    print(encrypt_weakness(part_a))
    print("Le Fin")
