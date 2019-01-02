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

def g(x, y):
    if (x is 'S' or x is 'D') and (y is 'S' or y is 'D'):
        return 3

    if (x is 'S' or x is 'E') and (y is 'S' or y is 'E'):
        return 9

    if (x is 'S' or x is 'P') and (y is 'S' or y is 'P'):
        return 1

    if (x is 'D' or x is 'B') and (y is 'B' or y is 'D'):
        return 1

    if (x is 'C' or x is 'D') and (y is 'C' or y is 'D'):
        return 8

    if (x is 'E' or x is 'D') and (y is 'E' or y is 'D'):
        return 2

    if (x is 'E' or x is 'H') and (y is 'E' or y is 'H'):
        return 8

    if (x is 'E' or x is 'R') and (y is 'E' or y is 'R'):
        return 2

    if (x is 'P' or x is 'H') and (y is 'P' or y is 'H'):
        return 4

    if (x is 'P' or x is 'Q') and (y is 'P' or y is 'Q'):
        return 15

    if (x is 'B' or x is 'A') and (y is 'B' or y is 'A'):
        return 2

    if (x is 'C' or x is 'F') and (y is 'C' or y is 'F'):
        return 3

    if (x is 'H' or x is 'Q') and (y is 'H' or y is 'Q'):
        return 4

    if (x is 'R' or x is 'F') and (y is 'R' or y is 'F'):
        return 2

    if (x is 'F' or x is 'G') and (y is 'F' or y is 'G'):
        return 2

    if (x is 'A' or x is 'C') and (y is 'A' or y is 'C'):
        return 2

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

def get_path(parents, current):
    total_path = [current]
    while current in parents.keys():
        current = parents[current]
        total_path.append(current)

    total_path.reverse()
    return total_path

def a_star(start, graph):
    expanded = []
    visited = [start]
    parents = dict()
    gScore = {start: 0}
    fScore = {start: 1000}

    while visited is not None:
        current = min(fScore, key=fScore.get)
        if current is 'G':
            return get_path(parents, current), expanded

        visited.remove(current)
        expanded.append(current)

        for neighbor in graph[current]:
            if neighbor in expanded:
                continue

            current_gScore = gScore[current] + g(current, neighbor)

            if neighbor not in visited:
                visited.append(neighbor)

            elif current_gScore >= gScore[neighbor]:
                continue

            parents[neighbor] = current
            gScore[neighbor] = current_gScore
            fScore[neighbor] = gScore[neighbor] + h(neighbor)

        del fScore[current]
    
path, expanded = a_star('S', graph)
expanded += 'G'
print('Nodes expanded: ')
print(expanded)
print('Path returned: ')
print(path)