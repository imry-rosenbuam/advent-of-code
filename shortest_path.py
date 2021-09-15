import math


def neighbors_set_find(u, maze):
    lst = list()
    for k in [-1, 1]:
        if 0 <= u[0] + k < len(maze):
            lst.append((u[0]+k, u[1]))
        if 0 <= u[1] + k < len(maze[u[0]]):
            lst.append((u[0], u[1]+k))
    return lst


def path_finder(maze):
    maze = maze.split("\n")
    last_node = (len(maze)-1, len(maze[len(maze)-1])-1)
    dist = {}
    prev = {}
    q = set()

    for i in range(len(maze)):
        for j in range(len(maze[i])):
            dist[(i, j)] = math.inf
            prev[(i, j)] = None
            q.add((i, j))

    dist[(0, 0)] = 0

    while len(q):
        i, j = min(q, key=lambda x: dist[x])  # u
        q.remove((i, j))

        neighbors_set = neighbors_set_find((i, j),maze)
        for neighbor in neighbors_set:
            if maze[i][j] == '.':
                alt = dist[(i, j)] + 1
                if alt < dist[neighbor]:
                    dist[neighbor] = alt
                    prev[neighbor] = alt
        
        if (i,j) == last_node:
            break

    if dist[last_node] == math.inf:
        return False
    else:
        return dist[last_node]


maze = "\n".join([
    "......",
    "......",
    "......",
    "......",
    ".....W",
    "....W."
])

xx = path_finder(maze)

le_fin = 1
