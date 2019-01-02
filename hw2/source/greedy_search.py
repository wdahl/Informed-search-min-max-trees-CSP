def h(x):
    if x is 'D':
        return 7
    
    if x is 'E':
        return 5

    if x is 'P':
        return 14

    if x is 'B':
        return 7

    if x is 'C':
        return 4

    if x is 'H':
        return 11

    if x is 'R':
        return 3

    if x is 'Q':
        return 12

    if x is 'A':
        return 5

    if x is 'F':
        return 2

    if x is 'G':
        return 0

graph = {'S': ['D', 'E', 'P'],
         'D': ['B', 'C', 'E', 'S'],
         'E': ['D', 'H', 'R', 'S'],
         'P': ['H', 'Q', 'S'],
         'B': ['A', 'D'],
         'C': ['A', 'D', 'F'],
         'H': ['E', 'P', 'Q'],
         'R': ['E', 'F'],
         'Q': ['H', 'P'],
         'A': ['B', 'C'],
         'F': ['C', 'G', 'R'],
         'G': ['F']}

visited = ['S']
path = ['S']
found = False

def greedy_search(start):
    global graph
    global visited
    global path
    global found

    if start is 'G':
        found = True
        return

    next_vertex = graph[start][0]

    for vertex in graph[start]:
        if vertex not in visited:
            if h(vertex) < h(next_vertex):
                next_vertex = vertex

    visited += next_vertex
    path += next_vertex

    greedy_search(next_vertex)
    
    if found is False:
        path.remove(next_vertex)
    
greedy_search('S')

print('Nodes expanded: ')
print(visited)
print('Path returned: ')
print(path)