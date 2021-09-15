import numpy as np
from numpy.lib.function_base import append
import pandas as pd
import re
from collections import Counter
file = "day20/input.txt"

tiles = {}


def symb_to_bin(s: str) -> int:
    if s == '#':
        return 1
    else:
        return 0


def edge_getter(tile: list) -> list:

    edge = list()
    arr = np.array(tile)

    for x in [0, len(arr)-1]:
        edge.append(arr[:, x])
        edge.append(arr[x, :])

    return edge


def corner_tiles_getter(tiles_: dict) -> list:

    corners = list()

    test = {}
    edges = {}
    s = {}
    for tile_num, tile in tiles_.items():
        edges_ = edge_getter(tile)
        for edge in edges_:
            e = tuple(edge.tolist())
            e_flip = tuple(np.flip(edge.tolist()))
            if edges.get(e):
                edges[e] += [tile_num]
            elif edges.get(e_flip):
                edges[e_flip] += [tile_num]
            else:
                edges[e] = [tile_num]

    edges_count = Counter([v[0] for k, v in edges.items() if len(v) < 2])

    corners = [k for k, v in edges_count.items() if v > 1]

    return corners


if __name__ == "__main__":

    with open(file, 'r') as reader:
        line = reader.readline()

        while line != "":
            if (match := re.match("Tile (\d+):", line)):
                tile_no = int(match.groups()[0])
                tile = list()
                line = reader.readline()

                while line not in ["\n", ""]:
                    row = list(map(symb_to_bin, line.strip()))
                    tile.append(row)
                    line = reader.readline()
                tiles[tile_no] = tile

            if line != "":
                line = reader.readline()

    corner_tiles = corner_tiles_getter(tiles)

    print("Answer for part A:")
    print(np.product(corner_tiles))
    print("Le Fin")
