import pandas
import numpy
import copy

file = "day11/input.txt"


def adjacent_seats(row: int, seat: int, seating: list) -> int:
    adjacent_seats_counter = 0

    if row == 0 and seat == 2:
        xx = 1
    lst = []
    lst2 = []
    # the extra one is to remind ourselves that range is not inclusive
    for i in range(max(0, row-1), min(len(seating), row + 1 + 1)):
        for j in range(max(0, seat-1), min(len(seating[row]), seat + 1 + 1)):
            if row != i or seat != j:
                if seating[i][j] == '#':
                    adjacent_seats_counter += 1

    if row == 0 and seat == 2:
        xx = 1

    return adjacent_seats_counter


def adjacent_seats_b(row: int, seat: int, seating: list) -> int:
    adjacent_seats_counter = 0
    max_len = max(len(seating[row]), len(seating))
    seat_len = len(seating[row])
    row_len = len(seating)
    sets = []
    directions = {}

    if row == 1 and seat == 2:
        xxx = 1

    for i in range(-1,2):
        for j in range(-1,2):
            if i!=0 or j!=0:
                k = 1
                while k < max_len:
                    r = row + i * k
                    s = seat + j * k
                    if r >=0 and r < row_len and s >= 0 and s < seat_len:
                        if seating[r][s] == '#':
                            directions[(i,j)] = 1
                            break
                        if seating[r][s] == 'L':
                            break
                    k += 1

    
    adjacent_seats_counter = len(directions)
    if row == 1 and seat == 2:
        xxx = 1
    return adjacent_seats_counter


def printing_seating(lst: list) -> None:

    string = ""

    rows = ["".join(row) for row in lst]

    string = "\n".join(rows)

    print(string)
    print("-------------------------------------------")


def game_of_seats(seating_arrangment: list) -> list:
    changes = 0
    # printing_seating(seating_arrangment)

    # instead of using a deepcopy we can enumerate all the change and only then apply them
    seating_arrangment2 = copy.deepcopy(seating_arrangment)

    for row in range(len(seating_arrangment)):
        for seat in range(len(seating_arrangment[row])):
            if seating_arrangment[row][seat] == '.':
                pass

            adjacent_seats_occupied = adjacent_seats(
                row, seat, seating_arrangment)
            if seating_arrangment[row][seat] == 'L' and adjacent_seats_occupied < 1:
                seating_arrangment2[row][seat] = '#'
                changes += 1
            elif seating_arrangment[row][seat] == '#' and adjacent_seats_occupied > 3:
                seating_arrangment2[row][seat] = 'L'
                changes += 1

    seating_arrangment = seating_arrangment2

    if changes < 1:
        return seating_arrangment
    else:
        return game_of_seats(seating_arrangment)


def game_of_seats_b(seating_arrangment: list) -> list:
    changes = 0
    #printing_seating(seating_arrangment)

    # instead of using a deepcopy we can enumerate all the change and only then apply them
    seating_arrangment2 = copy.deepcopy(seating_arrangment)

    for row in range(len(seating_arrangment)):
        for seat in range(len(seating_arrangment[row])):
            if seating_arrangment[row][seat] == '.':
                pass

            adjacent_seats_occupied = adjacent_seats_b(
                row, seat, seating_arrangment)
            if seating_arrangment[row][seat] == 'L' and adjacent_seats_occupied < 1:
                seating_arrangment2[row][seat] = '#'
                changes += 1
            elif seating_arrangment[row][seat] == '#' and adjacent_seats_occupied > 4:
                seating_arrangment2[row][seat] = 'L'
                changes += 1

    seating_arrangment = seating_arrangment2

    if changes < 1:
        return seating_arrangment
    else:
        return game_of_seats_b(seating_arrangment)


if __name__ == "__main__":
    seating = []
    with open(file, 'r') as reader:
        line = reader.readline()
        while line != "":
            seating.append(list(line.strip()))
            line = reader.readline()

    seating = game_of_seats(seating)
    seating_b = copy.deepcopy(seating)
    taken_seats = sum(
        [row[i] == '#' for row in seating for i in range(len(row))])
    print("Answer to Part A:")
    print(taken_seats)
    seating_b = game_of_seats_b(seating_b)
    taken_seats = sum([row[i] == '#' for row in seating_b for i in range(len(row))])
    print("Answer to Part B:")
    print(taken_seats)
    print("Le Fin")
