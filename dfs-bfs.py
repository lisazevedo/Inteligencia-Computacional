import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
import collections

graph = {
  'A' : set(['B','F']),
  'B' : set(['A']),
  'C' : set(['H', 'D']),
  'D' : set(['C', 'E']),
  'E' : set(['D', 'J']),
  'F' : set(['A', 'G']),
  'G' : set(['F', 'H']),
  'H' : set(['G', 'I', 'C']),
  'I' : set(['H', 'N']),
  'J' : set(['E']),
  'K' : set(['P']),
  'L' : set(['Q', 'M']),
  'M' : set(['L', 'R', 'N']),
  'N' : set(['M', 'I', 'O']),
  'O' : set(['N']),
  'P' : set(['K','U']),
  'Q' : set(['L', 'V']),
  'R' : set(['M', 'S']),
  'S' : set(['R', 'T']),
  'T' : set(['S', 'Z']),
  'U' : set(['P', 'V']),
  'V' : set(['U','Q', 'X']),
  'X' : set(['V', 'Y']),
  'Y' : set(['X', 'Z']),
  'Z' : set(['T', 'Y'])
}

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    #print(str(start) + " ", end="")
    print(str(start) +" ", end="")

    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

def bfs(graph, root):

    visited, queue = set(), collections.deque([root])
    visited.add(root)

    while queue:
        vertex = queue.popleft()
        print(str(vertex) + " ", end="")

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))


print("DFS: ")
dfs(graph, 'U')
print("\nDFS paths: ")
print(list(dfs_paths(graph, 'U', 'E')))

print('\n=======================================================================================')

print("BFS: ")
bfs(graph, 'U')
print("\nBFS paths: ")
print(list(bfs_paths(graph, 'U', 'E')))