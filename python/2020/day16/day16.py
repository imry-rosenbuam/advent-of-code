from io import TextIOWrapper
import numpy as np
import pandas as pd
import re

file = "day16/input.txt"

pattern = "([\w ]+): (\d+-\d+) or (\d+-\d+)"


def read_fields(line_: str, reader_: TextIOWrapper) -> dict:
    fields = {}
    line_itr = line_
    while line_itr != "\n":
        match = re.match(pattern, line_itr)
        field, group1, group2 = match.groups()
        fields[field] = [group1, group2]
        line_itr = reader_.readline()
    return fields


def read_my_ticket(line_: str) -> list:

    return list(map(int, line_.strip().split(',')))


def read_tickets(reader_: TextIOWrapper) -> list:
    ticket_line = reader_.readline().strip()
    tickets_ = list()

    while ticket_line != "":
        tickets_.append(list(map(int, ticket_line.split(','))))
        ticket_line = reader_.readline().strip()

    return tickets_


field_valid_values = {}

def valid_values(fields_: dict) -> set():
    values = set()
    global field_valid_values
    pattern_ = "(\d+)-(\d+)"
    for k,val in fields_.items():
        vals = set()
        for x in val:
            match = re.match(pattern_, x)
            a, b = match.groups()
            values |= set(range(int(a), int(b)+1))
            vals |= set(range(int(a),int(b)+1))
        field_valid_values[k] = vals
    return values


def fields_map(tickets_: list) -> dict:
    possible_fields = [list(field_valid_values.keys()) for _ in tickets_[0]]

    for tickt in tickets_:
        total_len = 0
        for i in range(len(tickt)):
            new_possible = list()
            for x in possible_fields[i]:
                    if tickt[i] in field_valid_values[x]: # I could have used list comprhension here but this form helped me identify a bug
                        new_possible.append(x)
            possible_fields[i] = new_possible
            if len(possible_fields[i]) == 1:
                val_to_remove = possible_fields[i][0]
                for j in range(len(tickt)):
                    if j!=i:
                        if val_to_remove in possible_fields[j]:
                            possible_fields[j].remove(val_to_remove)
    
    flag = 1

    while flag:
        for i in range(len(possible_fields)):
            if len(possible_fields[i]) == 1:
                val_to_remove = possible_fields[i][0]
                for j in range(len(tickt)):
                    if j != i:
                        if val_to_remove in possible_fields[j]:
                            possible_fields[j].remove(val_to_remove)
        if sum(map(len,possible_fields)) == len(possible_fields):
            flag =0

    return possible_fields

if __name__ == "__main__":
    with open(file, 'r') as reader:
        line = reader.readline()

        fields_dict = read_fields(line, reader)
        line = reader.readline()
        my_ticket = read_my_ticket(reader.readline())
        line = reader.readlines(2)
        tickets = read_tickets(reader)
        valid_vals = valid_values(fields_dict)

        error_rate = 0
        to_keep = list()
        for tckt in tickets:
            flag = 1
            for val in tckt:
                if val not in valid_vals:
                    error_rate += val
                    flag = 0
            if flag:
                to_keep.append(tckt)
        fields = fields_map(to_keep)
        to_calc = 1

        for i in range(len(fields)):
            if fields[i][0].find("departure") > -1:
                to_calc *= my_ticket[i]
        print("Answer to part A:")
        print(error_rate)
        print("Answer to part B")
        print(to_calc)
    print("Le Fin")
