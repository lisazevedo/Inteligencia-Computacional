import matplotlib
import matplotlib.pyplot as plt
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator
import numpy as np

maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0], 
        [0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0], 
        [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0], 
        [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0], 
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 
        [0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0], 
        [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0], 
        [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

def paths(graph, path, goal):
    if path[-1] == goal:
        yield path
        return
    for neighbor in graph[path[-1]]:
        if neighbor in path:
            continue
        yield from paths(graph, path + [neighbor], goal)

def plot_maze(maze):
    plt.pcolormesh(maze)
    plt.axes().set_aspect('equal')
    plt.xticks([]) 
    plt.yticks([])
    plt.show()

def graph(maze):
    rows=len(maze)
    cols=len(maze[0])

    graph={}

    for i in range(1, rows-1):
        for j in range(1, rows-1):
            if(maze[i][j]!=0):
                adj=[]  
                for ele in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                    if maze[ele[0]][ele[1]] == 1:
                        if(ele[0] <= 9 and ele[1] <= 9):
                            adj.append((ele[0],ele[1]))
                graph[(i,j)]=adj
    return graph

def get_smallest_path(graph, maze):
    _list = list(x for x in paths(graph(maze), [(9,9)], (1,1)))
    size = len(_list[0])
    id = 0
    for i in range(len(_list)):
        if size > len(_list[i]):
            size = len(_list[i])
            id = i
    return _list[id]

def change_maze(maze,shortest_path):
    for coord in shortest_path:
        maze[coord[0]][coord[1]] = 2
            
    return maze

shortest_path = get_smallest_path(graph, maze)
plot_maze(change_maze(maze,shortest_path))