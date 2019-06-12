import random
import numpy as np

def generate_maze(n, m, p):
    maze = []
    for i in range(n):
        l_i = ["."] * m
        for j in range(m):
            if random.random() > p:
                l_i[j] = "#"
        maze.append(l_i)

    return maze

def print_maze(maze):
    n = len(maze)
    for i in range(n):
        print(maze[i])


def neighs(maze, s_i, s_j):
    n = len(maze)
    m = len(maze[0])

    neighbors_s = []

    if (s_i) - 1 >= 0:
        neighbors_s.append((s_i-1, s_j))

    if (s_i) + 1 <= (n - 1):
        neighbors_s.append((s_i+1, s_j))

    if (s_j) - 1 >= 0:
        neighbors_s.append((s_i, s_j-1))

    if (s_j) + 1 <= (m - 1):
        neighbors_s.append((s_i, s_j+1))

    return neighbors_s


def mp(maze, s_i, s_j, e_i, e_j, visited):

    visited[s_i, s_j] = 1
    if s_i == e_i and s_j == e_j:
        return [(s_i, s_j)]

    s_path = []
    neighbors_s = neighs(maze, s_i, s_j)


    for neigh in neighbors_s:
        neigh_i, neigh_j = neigh[0], neigh[1]

        if maze[neigh_i][neigh_j] == "#":
            continue

        if visited[neigh_i, neigh_j] == 0:
            neigh_path = mp(maze, neigh_i, neigh_j, e_i, e_j, visited)
            if len(neigh_path) > 0:
                s_path = [(s_i, s_j)] + neigh_path
                break

    return s_path

n = 6
m = 7
p = 0.7
maze = generate_maze(n,m,p)
s_i, s_j = random.randint(0, n-1), random.randint(0, m-1)
e_i, e_j = random.randint(0, n-1), random.randint(0, m-1)

maze[s_i][s_j] = 'S'
maze[e_i][e_j] = 'E'


print_maze(maze)

visited = np.zeros((n, m))
maze_path = mp(maze, s_i, s_j, e_i, e_j, visited)

print("-----------------------------")
if len(maze_path) == 0:
    print("No path")
else:
    for p in range(1, len(maze_path)-1):
        p_i = maze_path[p][0]
        p_j = maze_path[p][1]
        maze[p_i][p_j] = '+'

print_maze(maze)
print(maze_path)


