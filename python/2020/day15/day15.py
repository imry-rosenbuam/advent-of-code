import numpy as np
import pandas as pd

file = "day15/input.txt"

if __name__ == "__main__":

    with open(file, 'r') as reader:
        line = reader.readline()
        numbers = list(map(int, line.split(',')))
        number_spoken = {}
        for i in range(len(numbers)-1):
            number_spoken[numbers[i]] = i + 1
            print((i+1,numbers[i]))

        counter = len(numbers) 
        num = numbers[counter - 1]

        while counter < 30000000:
            15716661
            30000000
            print((counter,num))
            if (last_time :=number_spoken.get(num,None)):
                new_num = counter - last_time
                number_spoken[num] = counter
                num = new_num
            else:
                number_spoken[num] = counter
                num = 0
            counter += 1

        print("Answer to the first part")
        print(num)
    print("Le Fin")
