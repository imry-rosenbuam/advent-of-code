import numpy as np
import pandas as pd

file="day5/input.txt"

letters_to_digits_dict={
    "F":0,
    "B":1,
    "L":0,
    "R":1
}

if __name__=="__main__":
    seat_ids_list=[]
    with open(file,'r') as reader:
        line=reader.readline()
        while line!="":
            line=line.strip()
            s=[str(letters_to_digits_dict[x]) for x in line]
            num="".join(s)
            col,row,seat_id = (int(num[-3:],2),int(num[:-3],2),int(num,2))
            print("row {0}, column {1}, Seat ID {2}".format(row,col,seat_id))
            seat_ids_list.append(seat_id)
            line=reader.readline()
    max_id=max(seat_ids_list)
    min_id=min(seat_ids_list)
    print("Part A answer is:")
    print("max seat id is {0}".format(max_id))
    missing_id=-1
    for i in range(min_id,max_id+1):
        try:
            seat_ids_list.remove(i)
        except:
            print("Part B answer is:")
            print(i)
            break
    print('Le Fin')
